# views.py
from rest_framework.decorators import api_view
from .models import ClimateData, Region, ClimateDataSummary
import requests
from django.shortcuts import render
from django.db import transaction
from .utils import parse_climate_text
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def fetch_climate_data(request):
    region_name = request.GET.get("region")
    parameter = request.GET.get("parameter")

    if not region_name or not parameter:
        return Response(
            {"error": "Missing region or parameter"}, status=status.HTTP_400_BAD_REQUEST
        )

    region_obj, _ = Region.objects.get_or_create(name=region_name, parameter=parameter)
    existing = ClimateData.objects.filter(region=region_obj).order_by("year")
    summary = ClimateDataSummary.objects.filter(region=region_obj).first()

    if existing.exists() and summary:
        return Response(
            {
                "data": list(existing.values()),
                "metadata": {"description": summary.description},
            },
            status=status.HTTP_200_OK,
        )
    url = f"https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{parameter}/date/{region_name}.txt"
    try:
        response = requests.get(url)
        response.raise_for_status()
        parsed = parse_climate_text(response.text)
        data_entries = parsed["data"]
        metadata = parsed["metadata"]

        with transaction.atomic():
            ClimateData.objects.bulk_create(
                [ClimateData(region=region_obj, **entry) for entry in data_entries]
            )
            ClimateDataSummary.objects.update_or_create(
                region=region_obj, defaults=metadata
            )

        return Response(
            {"data": data_entries, "metadata": metadata}, status=status.HTTP_200_OK
        )

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def summary_view(request):
    # Render frontend template
    return render(request, "summary.html")

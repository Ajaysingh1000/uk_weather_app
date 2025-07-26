# core/urls.py
from django.urls import path
from .views import summary_view, fetch_climate_data

urlpatterns = [
    path("", summary_view, name="summary"),
    path("fetch-climate-data/", fetch_climate_data),
]

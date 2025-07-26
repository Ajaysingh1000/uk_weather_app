# core/urls.py
from django.urls import path
from .views import summary_view , fetch_climate_data

urlpatterns = [
    # path('api/summary/', SummaryAPIView.as_view(), name='api-summary'),
    path('summary/', summary_view, name='summary'),
    path("fetch-climate-data/", fetch_climate_data),
]

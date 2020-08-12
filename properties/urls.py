from django.urls import path
from .views import index, PropertyDetailView, quick_property_search, LocationsView, AgentsView, advanced_property_search, city_view

app_name = 'properties'
urlpatterns = [
    path('', index, name="index"),
    path('<int:pk>', PropertyDetailView.as_view(), name="property_detail"),
    path('quickSearch', quick_property_search, name="quick_property_search"),
    path('locations', LocationsView.as_view(), name="locations"),
    path('meetTheTeam', AgentsView.as_view(), name="agents"),
    path('advancedSearch', advanced_property_search, name="advanced_property_search"),
    path('city/<slug:slug>', city_view, name="city_view"),
]


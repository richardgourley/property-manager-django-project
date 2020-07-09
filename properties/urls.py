from django.urls import path
from .views import index, PropertyDetailView, quick_property_search, LocationsView, AgentsView

app_name = 'properties'
urlpatterns = [
    path('', index, name="index"),
    path('<int:pk>', PropertyDetailView.as_view(), name="property_display"),
    path('quickSearch', quick_property_search, name="quick_property_search"),
    path('locations', LocationsView.as_view(), name="locations"),
    path('meet-the-team', AgentsView.as_view(), name="agents")
]


from django.urls import path
from .views import index, PropertyDetailView, quick_property_search

app_name = 'properties'
urlpatterns = [
    path('', index, name="index"),
    path('<int:pk>', PropertyDetailView.as_view(), name="property_display"),
    path('quickSearch', quick_property_search, name="quick_property_search")
]


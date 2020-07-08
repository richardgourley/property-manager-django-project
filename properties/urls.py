from django.urls import path
from .views import IndexView, PropertyDetailView

app_name = 'properties'
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('<int:pk>', PropertyDetailView.as_view(), name="property_display")
]

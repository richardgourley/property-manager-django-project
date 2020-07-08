from django.shortcuts import render
from django.views import generic
from .models import Property

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'properties/index.html'
	context_object_name = 'latest_properties'

	def get_queryset(self):
		return Property.objects.all().order_by('-pub_date')[:2]

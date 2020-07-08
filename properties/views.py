from django.shortcuts import render
from django.views import generic
from .models import Property, Office

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'properties/index.html'
	context_object_name = 'properties_and_offices'

	def get_queryset(self):
		properties = Property.objects.all().order_by('-pub_date')[:5]
		offices = Office.objects.all()
		return {'properties':properties, 'offices':offices}

class PropertyDetailView(generic.DetailView):
	model = Property
	template_name = 'properties/property-detail.html'

	def get_queryset(self):
		return Property.objects.all()

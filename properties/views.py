from django.shortcuts import render
from django.views import generic
from .models import Property, Office

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'properties/index.html'
	context_object_name = 'latest_properties'

	def get_queryset(self):
		return Property.objects.all().order_by('-pub_date')[:5]

class FooterView(generic.ListView):
	template_name = 'properties/footer.html'
	context_object_name = 'offices'

	def get_queryset(self):
		return Office.objects.all()

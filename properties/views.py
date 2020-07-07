from django.shortcuts import render
from django.views import generic

# Create your views here.
class IndexView(genric.ListView):
	template_name = 'index.html'

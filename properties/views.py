from django.shortcuts import render
from django.views import generic
from .models import Property, City
from .forms import QuickPropertySearchForm

# Create your views here.
def index(request):
    properties = Property.objects.all().order_by('-pub_date')[:5]
    cities = City.objects.all()
    form = QuickPropertySearchForm()
    return render(request, 'properties/index.html', {'properties':properties, 'cities':cities, 'form':form})

class PropertyDetailView(generic.DetailView):
    model = Property
    template_name = 'properties/property-detail.html'

    def get_queryset(self):
        return Property.objects.all()

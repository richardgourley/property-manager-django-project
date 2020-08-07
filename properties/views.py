from django.shortcuts import render
from django.views import generic
from .models import Property, City, Office, Agent
from .forms import QuickPropertySearchForm, AdvancedPropertySearchForm
from django.db.models import Q
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    cities = City.objects.all()
    form = QuickPropertySearchForm()
    return render(request, 'properties/index.html', {'cities':cities, 'form':form})

class PropertyDetailView(generic.DetailView):
    model = Property
    template_name = 'properties/property-detail.html'

    def get_queryset(self):
        return Property.objects.filter(pub_date__lte=timezone.now())

def quick_property_search(request):
    if request.method == 'POST':
        form = QuickPropertySearchForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city']
            properties = Property.objects.filter(city=city_name).filter(pub_date__lte=timezone.now())
            message = "We found 1 matching result" if len(properties) == 1 else "We found {} matching results.".format(len(properties))
            return render(request, 'properties/quick-property-search.html', {'properties':properties, 'message':message, 'form':form})
    else:
        form = QuickPropertySearchForm()

    return render(request, 'properties/quick-property-search.html', {'form':form})

class LocationsView(generic.ListView):
    template_name = 'properties/locations.html'
    context_object_name = 'offices'

    def get_queryset(self):
        return Office.objects.all()

class AgentsView(generic.ListView):
    template_name = 'properties/agents.html'
    context_object_name = 'agents'

    def get_queryset(self):
        return Agent.objects.filter().order_by('office')

def advanced_property_search(request):
    if request.method == 'POST':
        form = AdvancedPropertySearchForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city']
            max_price = form.cleaned_data['max_price']
            min_bedrooms = form.cleaned_data['min_bedrooms']
            properties = Property.objects.filter(
                Q(price__lte=max_price)
                & Q(city__city_name=city_name)
                & Q(bedrooms__gte=min_bedrooms)
            ).filter(pub_date__lte=timezone.now())
            message = "We found 1 matching result" if len(properties) == 1 else "We found {} matching results.".format(len(properties))
            return render(request, 'properties/advanced-property-search.html', {'properties':properties, 'message':message, 'form':form})
    else:
        form = AdvancedPropertySearchForm()

    return render(request, 'properties/advanced-property-search.html', {'form':form})
 



from django.shortcuts import render
from django.views import generic
from .models import Property, City,Office, Agent
from .forms import QuickPropertySearchForm, AdvancedPropertySearchForm
from django.db.models import Q
from django.utils import timezone

# Create your views here.
def index(request):
    properties = Property.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    cities = City.objects.all()
    coming_soon = False
    
    # If 0 properties in db - return 'coming_soon' which displays index-coming-soon-page
    if len(properties) == 0:
        coming_soon = True
        return render(request, 'properties/index.html', {'coming_soon':coming_soon})
    
    # If properties exist in db - return properties and cities - display normal index page
    form = QuickPropertySearchForm()
    return render(request, 'properties/index.html', {'properties':properties, 'cities':cities, 'form':form})

class PropertyDetailView(generic.DetailView):
    model = Property
    template_name = 'properties/property-detail.html'

    def get_queryset(self):
        return Property.objects.all()

def quick_property_search(request):
    if request.method == 'POST':
        form = QuickPropertySearchForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city']
            properties = Property.objects.filter(city=city_name)
            message = "We found 1 matching result" if len(search_results) == 1 else "We found {} matching results.".format(len(search_results))
            return render(request, 'properties/quick-property-search.html', {'properties':properties, 'message':message, 'form':form})
    else:
        form = QuickPropertySearchForm()

    return render(request, 'properties/quick-property-search.html', {'properties':[], 'message':'', 'form':form})

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
            search_results = Property.objects.filter(
                Q(price__lte=max_price)
                & Q(city__city_name=city_name)
                & Q(bedrooms__gte=min_bedrooms)
            )
            message = "We found 1 matching result" if len(search_results) == 1 else "We found {} matching results.".format(len(search_results))
            return render(request, 'properties/advanced-property-search.html', {'search_results':search_results, 'message':message, 'form':form})
    else:
        form = AdvancedPropertySearchForm()

    return render(request, 'properties/advanced-property-search.html', {'form':form})
 



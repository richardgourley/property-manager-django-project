from django.shortcuts import render
from django.views import generic
from .models import Property, City, Office, Agent
from .forms import QuickPropertySearchForm, AdvancedPropertySearchForm
from django.db.models import Q
from django.utils import timezone
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

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
            city = City.objects.get(city_name=city_name)
            return HttpResponseRedirect(reverse('properties:city_view', args=(city.slug,)))
    else:
        form = QuickPropertySearchForm()

    return render(request, 'properties/quick-property-search.html', {
        'form':form,
        })

def city_view(request, slug):
    city = get_object_or_404(City, slug=slug)
    properties = Property.objects.filter(city__slug=slug).filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    num_properties = properties.count()
    paginator = Paginator(properties, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = QuickPropertySearchForm()
    return render(request, 'properties/city.html', {
        'page_obj':page_obj,
        'num_properties':num_properties,
        'city':city,
        'form':form,
        }
    )

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
 



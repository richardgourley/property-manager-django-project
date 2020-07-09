from django.shortcuts import render
from django.views import generic
from .models import Property, City,Office
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

def quick_property_search(request):
    if request.method == 'POST':
        form = QuickPropertySearchForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city']
            search_results = Property.objects.filter(city=city_name)
            message = "We found 1 matching result" if len(search_results) == 1 else "We found {} matching results.".format(len(search_results))
            return render(request, 'properties/quick-property-search.html', {'search_results':search_results, 'message':message, 'form':form})
    else:
        form = QuickPropertySearchForm()

    return render(request, 'properties/quick-property-search.html', {'search_results':'', 'message':'', 'form':form})

class LocationsView(generic.ListView):
    template_name = 'properties/locations.html'
    context_object_name = 'offices'

    def get_queryset(self):
        return Office.objects.all()

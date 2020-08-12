from .models import Property
from django.utils import timezone

# Gets 5 latest properties for display on index, quick search and advanced search pages.

def latest_properties(request):
	return {
	    'latest_properties':Property.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
	}


	
	
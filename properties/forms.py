from django import forms
from .models import City

class QuickPropertySearchForm(forms.Form):
	city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label="SELECT A CITY")

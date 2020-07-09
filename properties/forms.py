from django import forms
from .models import City

class QuickPropertySearchForm(forms.Form):
	city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label="SELECT A CITY")

class AdvancedSearchForm(forms.Form):
	city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label="SELECT A CITY")
	max_price = forms.ChoiceField([
		('1400','1400'),
		('1300','1300'),
		('1200','1200'),
		('1100','1100'),
		('1000','1000'),
		('900','900'),
		('800','800'),
		])

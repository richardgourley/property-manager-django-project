from django import forms
from .models import City

class QuickPropertySearchForm(forms.Form):
	city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label=None)

class AdvancedPropertySearchForm(forms.Form):
	city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label=None)
	max_price = forms.ChoiceField(choices=[
		('1300','1300'),
		('1200','1200'),
		('1100','1100'),
		('1000','1000'),
		('900','900'),
		('800','800'),
		('700','700'),
	])
	min_bedrooms = forms.ChoiceField(choices=[
        ('1','1'),
        ('2','2'),
        ('3','3'),
	])


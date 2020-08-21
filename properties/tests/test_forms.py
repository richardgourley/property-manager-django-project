from django.test import TestCase, Client
from django.urls import reverse

from properties.forms import QuickPropertySearchForm, AdvancedPropertySearchForm

class QuickPropertySearchFormTests(TestCase):
	def test_empty_label_is_none(self):
		form = QuickPropertySearchForm()
		label = form.fields['city'].empty_label 
		self.assertEqual(None, label)

	
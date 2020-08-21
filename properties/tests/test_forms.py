from django.test import TestCase, Client
from django.urls import reverse

from properties.forms import QuickPropertySearchForm, AdvancedPropertySearchForm

class QuickPropertySearchFormTests(TestCase):
	def test_empty_label_is_none(self):
		form = QuickPropertySearchForm()
		label = form.fields['city'].empty_label 
		self.assertEqual(None, label)

class AdvancedPropertySearchFormTests(TestCase):
	def test_choices_quantity_max_price(self):
		len_choices = len(form.fields["max_price"].choices)
		self.assertTrue(len_choices == 7)

	def test_choices_quantity_min_bedrooms(self):
		len_choices = len(form.fields["min_bedrooms"].choices)
		self.assertTrue(len_choices == 3)

	def test_highest_max_price(self):
		highest_max_price = None
		for choice in form.fields["max_price"].choices:
		    if highest_max_price is None or int(choice[1]) > highest_max_price:
		        highest_max_price = int(choice[1])
		self.assertEqual(700, highest_max_price)

	def test_lowest_max_price(self):
		min_max_price = None
		for choice in form.fields["max_price"].choices:
		    if min_max_price is None or int(choice[1]) < min_max_price:
		        min_max_price = int(choice[1])
		self.assertEqual(700, min_max_price)

	def test_highest_min_bedrooms(self):
		highest_min_bedrooms = None
		for choice in form.fields["min_bedrooms"].choices:
		    if highest_min_bedrooms is None or int(choice[1]) > highest_min_bedrooms:
		        highest_min_bedrooms = int(choice[1])
		self.assertEqual(3, highest_min_bedrooms)

	def test_lowest_min_bedrooms(self):
		lowest_min_bedrooms = None
		for choice in form.fields["min_bedrooms"].choices:
		    if lowest_min_bedrooms is None or int(choice[1]) < lowest_min_bedrooms:
		        lowest_min_bedrooms = int(choice[1])
		self.assertEqual(1, lowest_min_bedrooms)





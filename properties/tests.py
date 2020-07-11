from django.test import TestCase, Client
from django.urls import reverse

import datetime
from django.utils import timezone

from .models import Office, City, Property, Agent

# Functions that create object instances for testing
def create_office():
	return Office.objects.create(office_name = office_name, address = address)

def create_city(city_name):
	return City.objects.create(city_name = city_name)

def create_agent(agent_name, email, office):
	return Agent.objects.create(agent_name = agent_name, email = email, office = office)

def create_property(property_name,bedrooms,bathrooms,description,pub_date,street_number,street_address,city,price):
	return Property.objects.create(
        property_name = property_name,
        bedrooms = bedrooms,
        bathrooms = bathrooms,
        description = description,
        pub_date = pub_date,
        street_number = street_number,
        street_address = street_address,
        city = city,
        price = price    
	)

# Classes that test models
class ModelTests(TestCase):
    def test_property_instance_is_type_property(self):
        city1 = create_city("Berlin")
        property1 = create_property(
            "Lovely new flat",3,2,"Best flat in the city", timezone.now(), 5, "Main Street", city1, 800
        )
        self.assertEqual(type(property1), Property)

    def test_city_name_rejects_numbers(self):
        city = create_city("1234")
        self.assertEqual(city.name)











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





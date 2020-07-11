from django.test import TestCase, Client
from django.urls import reverse

import datetime
from django.utils import timezone

from .models import Office, City, Property, Agent

'''
OBJECT INSTANCES FOR TESTING
'''
def create_office(office_name, address):
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

'''
MODEL TESTS
'''
class ModelTests(TestCase):
    def test_property_instance_is_type_property(self):
        city1 = create_city("Berlin")
        property1 = create_property(
            "Lovely new flat",3,2,"Best flat in the city", timezone.now(), 5, "Main Street", city1, 800
        )
        self.assertEqual(type(property1), Property)

    def test_city_name_is_string(self):
        city = create_city("Berlin")
        self.assertEqual(type(city.city_name), str)

    # FOREIGN KEY TESTS
    def test_deleting_property_doesnt_delete_city(self):
        city1 = create_city("Berlin")
        property1 = create_property(
            "Lovely new flat",3,2,"Best flat in the city", timezone.now(), 5, "Main Street", city1, 800
        )
        property2 = create_property(
            "Another lovely flat",2,2,"Second best flat in the city", timezone.now(), 57, "Main Street", city1, 900
        )
        property1.delete()
        property2.delete()
        self.assertTrue(city1)

    def test_deleting_office_doesnt_delete_agent(self):
        office1 = create_office("Berlin", "Main St")
        agent1 = create_agent("Bob", "bob@mail.com", office1)
        office1.delete()
        self.assertTrue(agent1)
    
    # MANY TO MANY RELATIONSHIP TESTS
    def test_assigning_property_to_agent_works(self):
        city1 = create_city("Berlin")
        property1 = create_property(
            "Lovely new flat",3,2,"Best flat in the city", timezone.now(), 5, "Main Street", city1, 800
        )
        office1 = create_office("Berlin", "Main St")
        agent1 = create_agent("Bob", "bob@mail.com", office1)
        # Assign property1 to "Bob" agent1
        agent1.property.add(property1)
        self.assertQuerysetEqual(agent1.property.all(), ['<Property: Lovely new flat>'])

    def test_after_agent_deletion_property_cant_access_agent(self):
        city1 = create_city("Berlin")
        property1 = create_property(
            "Lovely new flat",3,2,"Best flat in the city", timezone.now(), 5, "Main Street", city1, 800
        )
        office1 = create_office("Berlin", "Main St")
        agent1 = create_agent("Bob", "bob@mail.com", office1)
        # Assign property1 to "Bob" agent1
        agent1.property.add(property1)
        agent1.delete()
        self.assertQuerysetEqual(property1.agent_set.all(), [])


'''
VIEW TESTS
'''
# Need to test that 0 properties returns a message
class IndexTests(TestCase):
    def setup(self):
        self.client = Client

    # Test if 0 cities then we display a 'welcome message' instead of quick search
    def test_if_0_cities_displays_welcome_message_not_quick_search(self):
        response = self.client.get(reverse('properties:index'))
        contains = 'Welcome to Property Rentals' in str(response.content)
        self.assertIs(contains, True)

    def test_if_0_properties_coming_soon_message_appears(self):
        response = self.client.get(reverse('properties:index'))
        contains = 'coming soon' in str(response.content)
        self.assertIs(contains, True)

# Test returns 404 if pub_date is in future
# Test that a generic email is given to organize viewings IF no agent is assigned
class PropertyDetailViewTests(TestCase):
    pass

# Test that 0 properties returns a message in page
class QuickPropertySearchTests(TestCase):
    pass

# Test 0 offices displays a message
class LocationViewTests(TestCase):
    pass

# Test 0 agents displays a message
class AgentsViewTests(TestCase):
    pass




















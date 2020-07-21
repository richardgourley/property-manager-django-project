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

class IndexTests(TestCase):
    def setup(self):
        self.client = Client

    # Test 200 response status for home page
    def test_200_response_index_property_page(self):
        response = self.client.get(reverse('properties:index'))
        self.assertEqual(response.status_code, 200)

    # Test if 0 cities then we display a 'welcome message' instead of quick search
    def test_if_0_properties_displays_welcome_message_not_quick_search(self):
        response = self.client.get(reverse('properties:index'))
        contains = 'Welcome' in str(response.content)
        self.assertIs(contains, True)

    # Need to test that 0 properties returns a message
    def test_0_properties_returns_coming_soon_message(self):
        response = self.client.get(reverse('properties:index'))
        self.assertIn("Coming soon", str(response.content))

    # Test if properties with pub_date in the future don't appear
    def test_properties_pub_date_future_dont_appear(self):
        city1 = create_city("Berlin")
        '''
        property1 has future date, property2 has current date
        We expect property1 NOT to show so we expect ['<Property: property2>']
        '''
        property1 = create_property(
            "property1",3,2,"Best flat in the city", timezone.now() + datetime.timedelta(days=30), 5, "Main Street", city1, 800
        )
        property2 = create_property(
            "property2",3,2,"Best flat in the city", timezone.now(), 5, "Main Street", city1, 800
        )
        response = self.client.get(reverse('properties:index'))
        self.assertQuerysetEqual(response.context['properties'], ['<Property: property2>'])

    # Test newest property appears first
    def test_newest_property_appears_first_home_page(self):
        city1 = create_city("Berlin")
        property1 = create_property(
            "Timezone now",3,2,"Best flat in the city", timezone.now(), 5, "Main Street", city1, 800
        )
        property2 = create_property(
            "Timezone now - 20 days",3,2,"Best flat in the city", timezone.now() - datetime.timedelta(days=20), 5, "Main Street", city1, 800
        )
        response = self.client.get(reverse('properties:index'))
        self.assertEqual(response.context['properties'][0].property_name, "Timezone now")

class PropertyDetailViewTests(TestCase):
    # Test response status is 200 for property with pub_date in past
    def test_200_returned_if_pub_date_is_now_or_past(self):
        city1 = create_city("Berlin")
        property1 = create_property(
            "Lovely new flat",3,2,"Best flat in the city", timezone.now(), 5, "Main Street", city1, 800
        )
        response = self.client.get(reverse('properties:property_detail', args=(property1.id,)))
        self.assertEqual(response.status_code, 200)

    # Test returns 404 if pub_date is in future
    def test_404_returned_if_pub_date_in_future(self):
        city1 = create_city("Berlin")
        property1 = create_property(
            "Lovely new flat",3,2,"Best flat in the city", timezone.now() + datetime.timedelta(days=30), 5, "Main Street", city1, 800
        )
        response = self.client.get(reverse('properties:property_detail', args=(property1.id,)))
        self.assertEqual(response.status_code, 404)

    # Test that a generic email is given to organize viewings IF no agent is assigned
    def test_generic_email_given_if_no_agent_assigned(self):
        city1 = create_city("Berlin")
        property1 = create_property(
            "Lovely new flat",3,2,"Best flat in the city", timezone.now() + datetime.timedelta(days=30), 5, "Main Street", city1, 800
        )
        response = self.client.get(reverse('properties:property_detail', args=(property1.id,)))
        self.assertIn("info@mail.com", str(response.content))

class QuickPropertySearchTests(TestCase):
    # Test 200 returned for quick search
    def test_200_quick_search_page(self):
        response = self.client.get(reverse('properties:quick_property_search'))
        self.assertEqual(response.status_code, 200)

    # Test that 0 properties returns a message in page
    def test_0_properties_returns_coming_soon_message(self):
        response = self.client.get(reverse('properties:quick_property_search'))
        self.assertIn("Coming soon", str(response.content))

    def test_0_properties_returns_coming_soon_in_context(self):
        response = self.client.get(reverse('properties:quick_property_search'))
        self.assertEqual(response.context['coming_soon'], True)

class LocationViewTests(TestCase):
    # Test 200 returned for office locations page
    def test_200_response_locations_page(self):
        response = self.client.get(reverse('properties:locations'))
        self.assertEqual(response.status_code, 200)

    # Test 0 offices displays a message
    def test_0_offices_returns_coming_soon_message(self):
        response = self.client.get(reverse('properties:locations'))
        print(type(response.content))
        self.assertIn("coming soon", str(response.content))

class AgentsViewTests(TestCase):
    # Test 200 response status for agent page
    def test_200_response_status_agents_page(self):
        response = self.client.get(reverse('properties:agents'))
        self.assertEqual(response.status_code, 200)

    # Test 0 agents displays a message
    def test_0_agents_returns_generic_email_contact_address(self):
        response = self.client.get(reverse('properties:agents'))
        self.assertIn("info@mail.com", str(response.content))


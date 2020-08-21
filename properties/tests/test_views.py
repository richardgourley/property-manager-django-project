from django.test import TestCase, Client
from django.urls import reverse
from django.utils.text import slugify
import datetime
from django.utils import timezone

from properties.models import Office, City, Property, Agent

class IndexTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        city_name = "Las Vegas"
        slug = slugify(city_name)
        cls.city1 = City.objects.create(city_name=city_name, slug=slug)
        property_name1 = "Nice house 1"
        slug1 = slugify(property_name1)
        cls.property1 = Property.objects.create(
                property_name=property_name1,
                property_image="images/portfolio-9.jpg",
                bedrooms=2, bathrooms=2, description="A very nice house", 
                pub_date=timezone.now(), 
                street_number=5, street_address="Main Road", city=cls.city1, price=750,
                slug=slug
            )
        property_name2 = "Nice house 2"
        slug2 = slugify(property_name2)
        cls.property2 = Property.objects.create(
                property_name=property_name2,
                property_image="images/portfolio-9.jpg",
                bedrooms=2, bathrooms=2, description="A very nice house", 
                pub_date=timezone.now() - datetime.timedelta(days=20), 
                street_number=5, street_address="Main Road", city=cls.city1, price=750,
                slug=slug2
            )

    def test_index_200_direct_url(self):
        response = self.client.get('/properties/')
        self.assertEqual(response.status_code, 200)

    def test_index_200_reverse_url(self):
        response = self.client.get(reverse('properties:index'))
        self.assertEqual(response.status_code, 200)

    def test_custom_content_processor_returns_latest_properties(self):
        response = self.client.get(reverse('properties:index'))
        self.assertTrue(self.property1 in response.context["latest_properties"])
        self.assertTrue(self.property2 in response.context["latest_properties"])

    def test_index_uses_correct_template(self):
        response = self.client.get(reverse('properties:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'properties/index.html')

    def test_newer_pub_date_appears_first(self):
        response = self.client.get(reverse('properties:index'))
        self.assertEqual(response.context['properties'][0].property_name, "Nice house 1")

class IndexTestsNoProperties(self):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

    def test_0_properties_returns_coming_soon(self):
        response = self.client.get(reverse('properties:index'))
        self.assertIn(str(response.content), "Coming soon")

class PropertyDetailTests(self):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        city_name = "Las Vegas"
        slug = slugify(city_name)
        cls.city1 = City.objects.create(city_name=city_name, slug=slug)
        property_name1 = "Nice house 1"
        slug1 = slugify(property_name1)
        cls.property1 = Property.objects.create(
                property_name=property_name1,
                property_image="images/portfolio-9.jpg",
                bedrooms=2, bathrooms=2, description="A very nice house", 
                pub_date=timezone.now(), 
                street_number=5, street_address="Main Road", city=cls.city1, price=750,
                slug=slug
            )
        property_name2 = "Nice house 2"
        slug2 = slugify(property_name2)
        # Set with pub_date in the future
        cls.property2 = Property.objects.create(
                property_name=property_name2,
                property_image="images/portfolio-9.jpg",
                bedrooms=2, bathrooms=2, description="A very nice house", 
                pub_date=timezone.now() + datetime.timedelta(days=20), 
                street_number=5, street_address="Main Road", city=cls.city1, price=750,
                slug=slug2
            )

    def test_200_returned_if_pub_date_is_now_or_past(self):
        response = self.client.get(reverse('properties:property_detail', args=(self.property1.slug,)))
        self.assertEqual(response.status_code, 200)

    def test_404_returned_if_pub_date_in_future(self):
        response = self.client.get(reverse('properties:property_detail', args=(self.property2.slug,)))
        self.assertEqual(response.status_code, 404)

    def test_generic_email_given_if_no_agent_assigned(self):
        response = self.client.get(reverse('properties:property_detail', args=(self.property1.slug,)))
        self.assertIn("info@mail.com", str(response.content))

class QuickPropertySearchTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

    def test_200_quick_search_page(self):
        response = self.client.get(reverse('properties:quick_property_search'))
        self.assertEqual(response.status_code, 200)

    def test_quick_search_uses_correct_template(self):
        response = self.client.get(reverse('properties:quick_property_search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'properties/quick-property-search.html')

    def test_0_properties_returns_coming_soon_message(self):
        response = self.client.get(reverse('properties:quick_property_search'))
        self.assertIn("Coming soon", str(response.content))

    def test_quick_search_has_form(self):
        response = self.client.get(reverse('properties:quick_property_search'))
        self.assertIn(response.context, form)

class CityTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        city_name = "Las Vegas"
        slug = slugify(city_name)
        cls.city1 = City.objects.create(city_name=city_name, slug=slug)
        property_name1 = "Nice house 1"
        slug1 = slugify(property_name1)
        cls.property1 = Property.objects.create(
                property_name=property_name1,
                property_image="images/portfolio-9.jpg",
                bedrooms=2, bathrooms=2, description="A very nice house", 
                pub_date=timezone.now(), 
                street_number=5, street_address="Main Road", city=cls.city1, price=750,
                slug=slug
            )

    def test_incorrect_city_url_returns_404(self):
        response = self.client.get(reverse('properties:city', args=("nice-city",)))
        self.assertEqual(response.status, 404)

    def test_correct_city_url_returns_200(self):
        response = self.client.get(reverse('properties:city', args=(self.city1.slug,)))
        self.assertEqual(response.status, 200)

    def test_is_paginated(self):
        response = self.client.get('properties:city', args=(self.city1.slug,))
        self.assertTrue('is_paginated' in response.context)

class LocationTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

    def test_200_response_locations_page(self):
        response = self.client.get(reverse('properties:locations'))
        self.assertEqual(response.status_code, 200)

    def test_location_uses_correct_template(self):
        response = self.client.get(reverse('properties:locations'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'properties/locations.html')

    def test_0_offices_returns_coming_soon_message(self):
        response = self.client.get(reverse('properties:locations'))
        self.assertIn("Coming soon", str(response.content))

class AgentsViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

    def test_200_response_status_agents_page(self):
        response = self.client.get(reverse('properties:agents'))
        self.assertEqual(response.status_code, 200)

    def test_agents_uses_correct_template(self):
        response = self.client.get(reverse('properties:agents'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'properties/agents.html')

    def test_0_agents_returns_generic_email_contact_address(self):
        response = self.client.get(reverse('properties:agents'))
        self.assertIn("info@mail.com", str(response.content))

class AdvancedSearchTests(self):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

    def test_200_advanced_search_page(self):
        response = self.client.get(reverse('properties:advanced_property_search'))
        self.assertEqual(response.status_code, 200)

    def test_advanced_search_uses_correct_template(self):
        response = self.client.get(reverse('properties:advanced_property_search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'properties/advanced-property-search.html')

    def test_0_properties_returns_coming_soon_message(self):
        response = self.client.get(reverse('properties:advanced_property_search'))
        self.assertIn("Coming soon", str(response.content))

    def test_advanced_search_has_form(self):
        response = self.client.get(reverse('properties:advanced_property_search'))
        self.assertIn(response.context, form)
        




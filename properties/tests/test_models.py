from django.test import TestCase, Client
from django.utils.text import slugify
from properties.models import Property, City, Office, Agent
from django.urls import reverse
import datetime
from django.utils import timezone

class OfficeModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Office.objects.create(office_name="Los Angeles", address="Main St")

    def test_string(self):
        office1 = Office.objects.get(office_name="Los Angeles")
        self.assertEqual(str(office1), "Los Angeles")

class CityModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        city_name = "Las Vegas"
        slug = slugify(city_name)
        City.objects.create(city_name=city_name, slug=slug)

    def test_slug(self):
        city1 = City.objects.get(id=1)
        self.assertEqual(city1.slug, 'las-vegas')

    def test_verbose_names(self):
        verbose_names = {}
        city1 = City.objects.get(id=1)
        verbose_names["singular"] = city1._meta.verbose_name
        verbose_names["plural"] = city1._meta.verbose_name_plural
        self.assertEqual(verbose_names, {"singular":"city", "plural":"cities"})

    def test_city_name_field_unique(self):
        city1 = City.objects.get(id=1)
        self.assertEqual(city1._meta.get_field('city_name').unique, True)

    def test_slug_field_unique(self):
        city1 = City.objects.get(id=1)
        self.assertEqual(city1._meta.get_field('slug').unique, True)

    def test_city_string(self):
        city1 = City.objects.get(id=1)
        self.assertEqual(str(city1), city1.city_name)


class PropertyModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        city_name = "Las Vegas"
        slug = slugify(city_name)
        city1 = City.objects.create(city_name=city_name, slug=slug)
        property_name = "Nice house 1"
        slug = slugify(property_name)
        Property.objects.create(
                property_name=property_name,
                property_image="images/portfolio-9.jpg",
                bedrooms=2, bathrooms=2, description="A very nice house", 
                pub_date=timezone.now(), 
                street_number=5, street_address="Main Road", city=city1, price=750,
                slug=slug
            )

    def test_slug(self):
        property1 = Property.objects.get(id=1)
        self.assertEqual(property1.slug, "nice-house-1")

    def test_property_instance_is_type_property(self):
        property1 = Property.objects.get(id=1)
        self.assertEqual(type(property1), Property)

    def test_verbose_names(self):
        verbose_names = {}
        property1 = Property.objects.get(id=1)
        verbose_names["singular"] = property1._meta.verbose_name
        verbose_names["plural"] = property1._meta.verbose_name_plural
        self.assertEqual(verbose_names, {"singular":"property", "plural":"properties"})

    def test_property_name_field_unique(self):
        property1 = Property.objects.get(id=1)
        self.assertEqual(property1._meta.get_field('property_name').unique, True)

    def test_slug_field_unique(self):
        property1 = Property.objects.get(id=1)
        self.assertEqual(property1._meta.get_field('slug').unique, True)

    def test_pub_date_label(self):
        property1 = Property.objects.get(id=1)
        self.assertEqual(property1._meta.get_field('pub_date').verbose_name, 'date published')

    def test_city_is_nullable(self):
        property1 = Property.objects.get(id=1)
        self.assertEqual(property1._meta.get_field('city').null, True)

class AgentModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        office1 = Office.objects.create(office_name="Las Vegas", address="Main St")
        Agent.objects.create(agent_name="Jane", email="jane@propertyrentals.com", 
            office=office1)

    def test_agent_string(self):
        agent1 = Agent.objects.get(id=1)
        self.assertEqual(str(agent1), "Jane (Las Vegas)")

    def test_office_is_nullable(self):
        agent1 = Agent.objects.get(id=1)
        self.assertEqual(agent1._meta.get_field('property').null, True)






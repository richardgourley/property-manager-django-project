from django.db import models

# Create your models here.
class Office(models.Model):
	office_name = models.CharField(max_length=150)
	address = models.TextField(blank=False)

class City(models.Model):
	city_name = models.CharField(max_length=150)

class Property(models.Model):
	class Meta:
		verbose_name = 'property'
		verbose_name_plural = 'properties'
	property_name = models.CharField(max_length=150)
	bedrooms = models.PositiveSmallIntegerField(default=0)
	bathrooms = models.PositiveSmallIntegerField(default=0)
	description = models.TextField(blank=False)
	pub_date = models.DateTimeField('date published')
	street_number = models.PositiveSmallIntegerField(default=0)
	street_address = models.CharField(max_length=150)
	city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.property_name + '. CITY: ' + self.city.city_name

class Agent(models.Model):
	agent_name = models.CharField(max_length=150)
	email = models.EmailField()
	property = models.ManyToManyField(Property)
	# Set null=True because some agents might be freelance AND if we delete the office, the agent is still employed
	office = models.ForeignKey(Office, on_delete=models.SET_NULL, null=True)




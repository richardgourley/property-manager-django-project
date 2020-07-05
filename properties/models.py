from django.db import models

# Create your models here.
class Property(models.Model):
	property_name = models.CharField(max_length=150)
	bedrooms = models.IntegerField(deafult=0)
	bathrooms = models.IntegerField(default=0)
	description = models.TextField(blank=False)
	pub_date = models.DateTimeField('date published')
	address_number = models.PositiveSmallIntegerField(default=0)
	address_street = models.CharField(max_length=150)
	address_city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

class Agent(models.Model):
	agent_name = models.CharField(max_length=150)
	email = models.EmailField()
	property = models.ManyToManyField(Property)
	# Set null=True because some agents might be freelance AND if we delete the office, the agent is still employed
	office = models.ForeignKey(Office, on_delete=models.SET_NULL, null=True)

class Office(models.Model):
	office_name = models.CharField(max_length=150)
	address = models.TextField(blank=False)

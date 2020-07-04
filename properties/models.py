from django.db import models

# Create your models here.
class Property(models.Model):
	property_name = models.CharField(max_length=150)
	bedrooms = models.IntegerField(deafult=0)

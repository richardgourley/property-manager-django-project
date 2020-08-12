from django.db import models
from django.urls import reverse

# Create your models here.
class Office(models.Model):
    office_name = models.CharField(max_length=150, help_text="How will this office be know geographically? Normally this would be the name of the city the office is in.")
    address = models.TextField(blank=False, help_text="HIT ENTER TO USE A NEW LINE")

    def __str__(self):
        return self.office_name

class City(models.Model):
    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'
    city_name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200)

    def get_absolute_url(self):
        return reverse('city', args=[str(self.city_name)])
    
    def __str__(self):
        return self.city_name

class Property(models.Model):
    class Meta:
        verbose_name = 'property'
        verbose_name_plural = 'properties'
    property_name = models.CharField(max_length=150, help_text="Eg. A beautiful 2 bedroom house with a large garden.")
    property_image = models.ImageField(upload_to="images", null=True)
    bedrooms = models.PositiveSmallIntegerField(default=0)
    bathrooms = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(blank=False)
    pub_date = models.DateTimeField('date published', help_text="Either click 'Today' and 'Now' or you can enter a date in the past.")
    street_number = models.PositiveSmallIntegerField(default=0, help_text="Leave default as 0 if you haven't been given an exact street number.")
    street_address = models.CharField(max_length=150)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=False)
    price = models.DecimalField(default=750, max_digits=7, decimal_places=2)

    def __str__(self):
        return self.property_name

    def display_agents(self):
        agents = self.agent_set.all()
        return (', ').join(str(agent) for agent in agents)

    display_agents.short_description = "AGENT/S"

class Agent(models.Model):
    agent_name = models.CharField(max_length=150)
    email = models.EmailField()
    property = models.ManyToManyField(Property, help_text="Assign this agent to a property")
    # Set null=True because some agents might be freelance AND if we delete the office, the agent is still employed
    office = models.ForeignKey(Office, on_delete=models.SET_NULL, null=True)

    '''
    Return the office name next to the agent - helps in defining agents in admin page
    '''
    def __str__(self):
        return self.agent_name + ' (' + str(self.office) + ')'




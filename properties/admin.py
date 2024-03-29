from django.contrib import admin
from .models import Property, Agent, Office, City

# Register your models here.
class AgentInLine(admin.TabularInline):
    model = Agent.property.through
    '''
    Override verbose name and verbose plural name only for the admin form to offer more instruction
    '''
    verbose_name = "AGENT"
    verbose_name_plural = "AGENTS  - ASSIGN AN AGENT/ AGENTS TO THIS PROPERTY"

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['property_name', 'pub_date', 'bedrooms', 'bathrooms', 'city', 'display_agents', 'price']
    list_filter = ['pub_date', 'city']
    prepopulated_fields = {'slug':('property_name',)}
    
    inlines = [
        AgentInLine,
    ]

    fieldsets = (
        ('General Information', {
            'fields': ('property_name','slug','property_image','city','street_number','street_address')
        }),
        ('Details', {
            'fields': ('description', 'bedrooms','bathrooms')
        }),
        ('Date Published and Price', {
            'fields': ('pub_date', 'price')
        }),
    )

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['agent_name', 'email', 'office']

    fields = ['agent_name', 'email', 'office']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name',)
    prepopulated_fields = {'slug': ('city_name',)}

admin.site.register(Office)

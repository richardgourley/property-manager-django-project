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

class PropertyAdmin(admin.ModelAdmin):
    list_display = ['property_name', 'pub_date', 'bedrooms', 'bathrooms', 'city', 'get_agents', 'price']
    
    def get_agents(self, obj):
        agents = obj.agent_set.all()
        return (', ').join(str(agent) for agent in agents)

    get_agents.short_description = "AGENT/S"

    inlines = [
        AgentInLine,
    ]

class AgentAdmin(admin.ModelAdmin):
    list_display = ['agent_name', 'email', 'office']

admin.site.register(Property, PropertyAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Office)
admin.site.register(City)

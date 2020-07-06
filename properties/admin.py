from django.contrib import admin
from .models import Property, Agent, Office, City

# Register your models here.
class AgentInLine(admin.StackedInline):
	model = Agent.property.through

class PropertyAdmin(admin.ModelAdmin):
	inlines = [
        AgentInLine,
	]

admin.site.register(Property, PropertyAdmin)
admin.site.register(Agent)
admin.site.register(Office)
admin.site.register(City)



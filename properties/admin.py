from django.contrib import admin
from .models import Property, Agent, Office

# Register your models here.
class AgentInLine(admin.TabularInline):
	model = Agent.property.through

class PropertyAdmin(admin.ModelAdmin):
	inlines = [
        AgentInLine,
	]

admin.site.register(Property, PropertyAdmin)


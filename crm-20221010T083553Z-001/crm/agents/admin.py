from django.contrib import admin
from .models import agent
from import_export.admin import ImportExportModelAdmin
from .models import Ticket

@admin.register(agent)
class AgentAdmin(ImportExportModelAdmin):
    list_display = ('user','agent_name','organisation','phone_number','email')



# Register your models here.
class TicketAdmin(admin.ModelAdmin):
  date_hierarchy = 'created_at'
  list_filter = ('status', 'assignee')
  list_display = ('id', 'customer_name', 'status', 'assignee', 'subject', 'updated_at')
  search_fields = ['customer_name','status']
admin.site.register(Ticket, TicketAdmin)    

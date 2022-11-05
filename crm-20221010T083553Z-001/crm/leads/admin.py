from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Customer, Lead, catagory, lead_activity, lead_communication, product ,quotation



admin.site.register(catagory)
admin.site.register(product)


@admin.register(Lead)
class LeadAdmin(ImportExportModelAdmin):
    list_display = ('first_name','last_name','agent','size','location','phone_number','designation','email','source','stage','status','pincode',)

admin.site.register(lead_activity)
admin.site.register(lead_communication)
admin.site.register(Customer)
admin.site.register(quotation)
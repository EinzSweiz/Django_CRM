from django.contrib import admin
from crm.models import Records

@admin.register(Records)
class RecordsAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'phone', 'address', 'city', 'state', 'zipcode']
    readonly_fields = ['created_at']
    list_display = ('last_name', 'first_name', 'address', 'city', 'created_at') 
    list_editable = ('first_name',)
    list_display_links = ('last_name',)

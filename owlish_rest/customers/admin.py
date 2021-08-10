from django.contrib import admin
from .models import Customer
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('pk','first_name','last_name','title','lat','lng')
    list_display_links = ('first_name','last_name')
    #list_editable = ('phone_number','website','picture')
    search_fields = ('first_name','last_name')
    
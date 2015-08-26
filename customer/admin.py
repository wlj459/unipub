from django.contrib import admin
from models import Customer
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'permission')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'integral')

admin.site.register(Customer, CustomerAdmin)

from django.contrib import admin
from models import Customer, Company
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'permission')

admin.site.register(Customer)
admin.site.register(Company, CompanyAdmin)

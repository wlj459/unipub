from django.contrib import admin
from models import Customer, Head, School
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'integral', 'permission', 'type')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Head)
admin.site.register(School)

from django.contrib import admin
from models import Customer, Head
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'integral', 'permission', 'type')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Head)

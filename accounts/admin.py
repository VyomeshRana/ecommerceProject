from django.contrib import admin
from .models import customerModel,vendorModel

# Register your models here.

admin.site.register(customerModel)
admin.site.register(vendorModel)

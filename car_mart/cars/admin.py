from django.contrib import admin

# Register your models here.
from .models import Carcompany,CEO,CarModel,FuelType
admin.site.register(CarModel)
admin.site.register(Carcompany)
admin.site.register(CEO)
admin.site.register(FuelType)

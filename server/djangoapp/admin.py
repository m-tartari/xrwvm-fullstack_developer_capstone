from django.contrib import admin
from .models import CarMake, CarModel


# CarModelInline class
class CarModelInline(admin.TabularInline):  # or `admin.StackedInline`
    model = CarModel
    extra = 0  # number of empty CarMakes to fill


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    model = CarModel


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    model = CarMake
    inlines = [CarModelInline]


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)

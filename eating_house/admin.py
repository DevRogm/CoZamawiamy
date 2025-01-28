from django.contrib import admin

from eating_house.models import EatingHouse, Address, Meal


@admin.register(EatingHouse)
class EatingHouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'street_number', 'apartment_number', 'postal_code')

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'meal_type')

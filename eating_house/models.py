from django.db.models import ForeignKey

from eating_house.constants import MealType, DEFAULT_MEAL_TYPE
from server.settings import LANGUAGE_CODE
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.db import models


class Address(models.Model):
    country = CountryField(verbose_name="Country", blank_label="(select country)", default=LANGUAGE_CODE)
    city = models.CharField(verbose_name="City", max_length=64)
    street = models.CharField(verbose_name="Street", max_length=64)
    street_number = models.CharField(verbose_name="Street number", max_length=16)
    apartment_number = models.CharField(verbose_name="Apartment number", max_length=16, null=True, blank=True)
    postal_code = models.CharField(verbose_name="Postal code", max_length=64)

    class Meta:
        unique_together = ('country', 'city', 'street', 'street_number', 'postal_code')
        verbose_name = "Address"
        verbose_name_plural = "Address"

    def __str__(self):
        return self.get_full_address()

    def get_full_address(self):
        full_address = f"{self.street} {self.street_number}"
        full_address += f"/{self.apartment_number}, " if self.apartment_number else ", "
        full_address += f"{self.postal_code} {self.city}"
        return full_address


class EatingHouse(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255, unique=True)
    phone_number = PhoneNumberField(verbose_name="Phone number", region=LANGUAGE_CODE)
    address = models.OneToOneField(Address, verbose_name="Address", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Eating House"
        verbose_name_plural = "Eating Houses"

    def __str__(self):
        return self.name


class Meal(models.Model):
    eating_house = ForeignKey(EatingHouse, verbose_name="Eating house", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Name", max_length=128)
    description = models.TextField(verbose_name="Description", max_length=512)
    price = models.DecimalField(verbose_name="Price", max_digits=5, decimal_places=2)
    meal_type = models.CharField(max_length=20, choices=MealType.choices, default=DEFAULT_MEAL_TYPE)

    class Meta:
        unique_together = ('eating_house', 'name')
        verbose_name = "Meal"
        verbose_name_plural = "Meals"

    def __str__(self):
        return self.name

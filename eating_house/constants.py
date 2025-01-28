from django.db import models

class MealType(models.TextChoices):
    SOUP = 'soup', 'Soup'
    PIZZA = 'pizza', 'Pizza'
    PASTA = 'pasta', 'Pasta'
    SALAD = 'salad', 'Salad'
    APPETIZER = 'appetizer', 'Appetizer'
    VEGETARIAN = 'vegetarian', 'Vegetarian Dish'
    VEGAN = 'vegan', 'Vegan Dish'
    DESSERT = 'dessert', 'Dessert'
    DRINK = 'drink', 'Drinks'
    COCKTAIL = 'cocktail', 'Cocktail'
    FAST_FOOD = 'fast_food', 'Fast Food'
    BREAKFAST = 'breakfast', 'Breakfast'
    DINNER = 'dinner', 'Dinner'
    SNACK = 'snack', 'Snack'
    BREAD = 'bread', 'Bread'
    SUSHI = 'sushi', 'Sushi'
    INTERNATIONAL = 'international', 'International Dish'
    GRILLED = 'grilled', 'Grilled Dish'
    CREAM_SOUP = 'cream_soup', 'Cream Soup'

DEFAULT_MEAL_TYPE = MealType.DINNER
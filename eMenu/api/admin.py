from django.contrib import admin
from . import models


@admin.register(models.Menu)
class Menu(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'addition_date', 'update_date')
    fields = ('name', 'description')


@admin.register(models.Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'menu', 'addition_date', 'update_date', 'price', 'preparation_time',
                    'vegetarian', 'image')
    fields = ('name', 'description', 'menu', 'price', 'preparation_time', 'vegetarian', 'image')

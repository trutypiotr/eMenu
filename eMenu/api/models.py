from django.db import models
from . import managers


class BaseModel(models.Model):
    description = models.CharField(max_length=128)
    addition_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    name = None

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Menu(BaseModel):
    name = models.CharField(max_length=64, unique=True)
    objects = managers.MenuManager()


class Dish(BaseModel):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='dishes')
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    preparation_time = models.DurationField()
    vegetarian = models.BooleanField()
    image = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'dishes'

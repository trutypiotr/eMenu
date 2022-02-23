from django.db import models
from django.db.models import Count


class MenuManager(models.Manager):
    def with_dishes(self):
        return self.annotate(num_of_dishes=Count('dishes'))

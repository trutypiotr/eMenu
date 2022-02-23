from django_filters import rest_framework as filter
from . import models


class MenuFilter(filter.FilterSet):
    ordering = filter.OrderingFilter(
        fields=(
            ('name', 'name'),
            ('num_of_dishes', 'num_of_dishes')
        )
    )

    def filter_queryset(self, queryset):
        queryset = queryset.filter(num_of_dishes__gt=0)
        return super().filter_queryset(queryset)

    class Meta:
        model = models.Menu
        fields = ('name', 'addition_date', 'update_date')




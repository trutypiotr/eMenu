from rest_framework import permissions, mixins, viewsets
from rest_framework.parsers import MultiPartParser

from . import serializers
from . import models
from .filters import MenuFilter


class MenuViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.Menu.objects.with_dishes()
    filterset_class = MenuFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.MenuSerializer
        else:
            return serializers.MenuDetailSerializer


class DishImageViewSet(viewsets.GenericViewSet,
                       mixins.UpdateModelMixin):
    queryset = models.Dish.objects.all()
    serializer_class = serializers.DishImageSerializer
    parser_classes = (MultiPartParser, )

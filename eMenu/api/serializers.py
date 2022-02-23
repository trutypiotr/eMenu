from rest_framework import serializers
from . import models


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dish
        fields = ('id', 'name', 'description', 'price', 'preparation_time', 'vegetarian')


class DishImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dish
        fields = ('image', )


class MenuSerializer(serializers.ModelSerializer):
    num_of_dishes = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.Menu
        fields = ('id', 'name', 'description', 'num_of_dishes')


class MenuDetailSerializer(MenuSerializer):
    dishes = DishSerializer(many=True)

    def create(self, validated_data):
        dishes_data = validated_data.pop('dishes')
        menu = models.Menu.objects.create(**validated_data)
        for dish_data in dishes_data:
            models.Dish.objects.create(menu=menu, **dish_data)
        return menu

    class Meta(MenuSerializer.Meta):
        fields = MenuSerializer.Meta.fields + ('dishes',)

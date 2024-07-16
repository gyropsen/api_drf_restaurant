from rest_framework import generics

from restaurant_menu.models import FoodCategory
from restaurant_menu.serializers import FoodListSerializer


class FoodCategoryListAPIView(generics.ListAPIView):
    """
    Эндпоинт для получения всех публичных привычек
    """

    queryset = FoodCategory.objects.order_by("pk")
    serializer_class = FoodListSerializer

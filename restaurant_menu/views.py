from django.db.models import Prefetch
from rest_framework import generics
from rest_framework.response import Response

from restaurant_menu.models import Food, FoodCategory
from restaurant_menu.serializers import FoodListSerializer


class FoodCategoryListAPIView(generics.ListAPIView):
    """
    Эндпоинт для получения всех разделов меню, с фильтром еды по публикации
    """

    queryset = FoodCategory.objects.prefetch_related(
        Prefetch("food", queryset=Food.objects.filter(is_publish=True))
    ).order_by("pk")
    serializer_class = FoodListSerializer

    def list(self, request, *args, **kwargs):
        """
        Список запросов с фильтрацией по foods
        """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        data = [food_category for food_category in serializer.data if food_category.get("foods")]
        return Response(data)

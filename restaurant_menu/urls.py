from django.urls import path

from restaurant_menu.apps import RestaurantMenuConfig
from restaurant_menu.views import FoodCategoryListAPIView

app_name = RestaurantMenuConfig.name

urlpatterns = [
    path("v1/foods/", FoodCategoryListAPIView.as_view(), name="foods"),
]

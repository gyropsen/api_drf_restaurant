from django.contrib import admin

from restaurant_menu.models import Food, FoodCategory


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    """
    Класс отображения категории еды в админке
    """

    list_display = (
        'pk',
        'name_ru',
        'order_id',
    )


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    """
    Класс отображения еды в админке
    """

    list_display = (
        'pk',
        'name_ru',
        'category',
        'is_publish'
    )

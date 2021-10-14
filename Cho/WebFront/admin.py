from django.contrib import admin
from .models import Category, Station, Dish, Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ['address']

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['station', 'date', 'status']
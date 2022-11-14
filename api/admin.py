from django.contrib import admin
from .models import FoodSale
from import_export.admin import ImportExportModelAdmin


# Register your models here.

@admin.register(FoodSale)
class FoodSaleAdmin(ImportExportModelAdmin):
    list_display = ('date', 'region', 'city', 'category', 'product', 'quantity', 'unit_price')



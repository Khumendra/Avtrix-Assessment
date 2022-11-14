from .models import FoodSale
from rest_framework import serializers


class FoodSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodSale
        fields = ['id',
                  'date',
                  'region',
                  'city',
                  'category',
                  'product',
                  'quantity',
                  'unit_price'
                  ]

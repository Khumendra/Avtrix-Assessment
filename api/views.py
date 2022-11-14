from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from tablib import Dataset
from django.contrib import messages
from django_filters import rest_framework as filters

from .resources import FoodSaleResource
from .models import FoodSale
from .serializers import FoodSaleSerializer


# Create your views here.
def index(request):
    if request.method == 'POST':
        food_resources = FoodSaleResource()
        dataset = Dataset()

        new_foodsale_data = request.FILES['myfile']

        # check if file format is xlsx
        if not new_foodsale_data.name.endswith('xlsx'):
            messages.info(request, 'Wrong format  supports xlsx format')
            return render(request, 'index.html')

        imported_data = dataset.load(new_foodsale_data.read(), format='xlsx')

        for data in imported_data:
            print(data)
            value = FoodSale(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],

            )
            value.save()
    return render(request, 'index.html')


class FoodSaleViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = FoodSale.objects.all()
    serializer_class = FoodSaleSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id', 'product', 'category')
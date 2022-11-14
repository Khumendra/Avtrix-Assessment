from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from pprint import pprint

app_name = 'api'

routers = DefaultRouter()
routers.register(r'api', views.FoodSaleViewSet)
pprint(routers.urls)
urlpatterns = [
    path('', views.index),
    path('', include(routers.urls))
]

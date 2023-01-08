from django.urls import path
from . import views

urlpatterns = [
    path('getPrice', views.getPrice, name="getPrice"),
    path('ccyPrice', views.getCcyPrice, name="getCcyPrice"),
    path('topLists', views.getTopExchanges, name="getTopExchanges"),
    path('indexValues', views.singleIndexValue, name="singleIndexValue"),
    ]
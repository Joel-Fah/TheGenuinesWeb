from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home, name = 'Home'),
    path('order/', Order, name = 'Order'),
    path('modelform/', GetOrder, name = 'GetOrder'),
    path('developer/', Developer, name = 'Developer'),
    path('portfolio-details/', PortfolioDetails, name = 'PortfolioDetails'),
]
from django.urls import path
from .views import checkout
from .views import status, OrdersList

app_name = 'payment'

urlpatterns = [
    path('', checkout.as_view(), name="checkout"),
    path('status/', status),
    path('orders/', OrdersList.as_view(), name="orders")
]

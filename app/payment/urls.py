from django.urls import path
from .views import checkout
from .views import status
urlpatterns = [
    path('', checkout.as_view(), name="checkout"),
    path('status/', status)
]

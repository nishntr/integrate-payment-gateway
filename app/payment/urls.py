from django.urls import path
from .views import checkout
from .views import status, OrdersList, statusRedirect
from django.views.decorators.csrf import csrf_exempt

app_name = 'payment'

urlpatterns = [
    path('', checkout.as_view(), name="checkout"),
    path('statusRedirect/', csrf_exempt(statusRedirect.as_view()),
         name="statusRedirect"),
    path('status/<str:id>/', status.as_view(), name="status"),
    path('orders/', OrdersList.as_view(), name="orders")
]

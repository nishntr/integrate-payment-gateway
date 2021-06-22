from .views import registerUser, loginUser, logoutUser
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerUser, name='register')
]

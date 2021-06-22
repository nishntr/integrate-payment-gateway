from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=30,)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email']

    def get_name(self):
        return self.name

    def __str__(self):
        return self.username

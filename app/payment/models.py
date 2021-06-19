from django.db import models
# from django.contrib.auth import User

# Create your models here.


class Transaction(models.Model):
    txnid = models.CharField(max_length=40)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    product = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.txnid

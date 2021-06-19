from django.forms import ModelForm
from .models import Transaction


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['txnid', 'amount', 'product', 'name', 'email']

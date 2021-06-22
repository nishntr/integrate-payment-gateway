from django.forms import ModelForm
from .models import Transaction


class TransactionForm(ModelForm):

    class Meta:
        model = Transaction
        fields = ['txnid', 'amount', 'product', 'email']


class ExtraFields(TransactionForm):
    product = Transaction.get_product_name()
    name = Transaction.get_username()

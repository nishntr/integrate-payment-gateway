from accounts.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
import random
import string
import hashlib
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from .models import Transaction
from payment.models import Product


# sha512 vd2Y1X|k8WnSppfWj5dO5|10.00|iPhone|PayU User|test@gmail.com|||||||||||Brg97QyF
# test card 5123-4567-8901-2346 4012-0010-3714-1112 123 123456


class checkout(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()

        print([request.session[x] for x in request.session.keys()])

        return render(request, 'checkout.html', {'products': products})

    def post(self, request, *args, **kwargs):
        key = 'gtKFFx'
        salt = 'wia56q6O'
        product_id = request.POST.get('pk')
        name = request.user.name
        email = request.user.email

        txnid = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=24))

        product = Product.objects.get(pk=product_id)
        amount = str(product.price)

        strg = key + '|' + txnid + '|' + amount + '|' + \
            product.name + '|' + name + '|' + email + '|||||||||||' + salt
        hash = hashlib.sha512(strg.encode()).hexdigest()

        context = {
            'key': key,
            'salt': salt,
            'txnid': txnid,
            'amount': amount,
            'product': product.name,
            'name': name,
            'email': email,
            'surl': 'http://localhost:8000/statusRedirect/',
            'furl': 'http://localhost:8000/statusRedirect/',
            'hash': hash

        }

        t = Transaction(txnid=txnid,
                        product=product, user=request.user, email=email)
        t.save()

        return render(request, 'redirect.html', context=context)


# @method_decorator(csrf_exempt, name='dispatch')
class statusRedirect(View):

    def post(self, request, *args, **kwargs):
        status = request.POST.get('status')
        txnid = request.POST.get('txnid')
        print(request.session.keys())

        t = Transaction.objects.get(txnid=txnid)
        if status == 'success':
            t.status = True
            t.save()
            print("completed for:" + t.user.name)

        # context = {
        #     'txnid': txnid,
        #     'status': status,
        #     'product': t.product.name,

        # }
        # request.session['txnid'] = txnid
        # request.session['status'] = status
        # request.session['product'] = t.product.name

        return redirect(t)


class status(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        print(kwargs)
        txnid = kwargs['id']
        t = Transaction.objects.get(txnid=txnid)
        context = {
            'txnid': txnid,
            'status': t.status,
            'product': t.product.name,

        }
        return render(request, 'status.html', context=context)


class OrdersList(LoginRequiredMixin, ListView):
    login_url = '/login/'

    model = Transaction
    template_name = "orders.html"

    def get_queryset(self):
        return self.request.user.orders.all().order_by('-date')

# @login_required(login_url='/login/')
# @csrf_exempt
# def status(request):
#     if request.method == "POST":
#         data = dict(request.POST)
#         status = request.POST.get('status')
#         txnid = request.POST.get('txnid')

#         t = Transaction.objects.get(txnid=txnid)
#         if status == 'success':
#             t.status = True
#             t.save()
#             print("completed for:" + t.user.name)

#         context = {
#             'txnid': txnid,
#             'status': status,
#             'product': t.product.name,

#         }

#         return render(request, 'status.html', context=context)

    # Array
    # (
    #     [mihpayid] => 13297721729
    #     [mode] => CASH
    #     [status] => success
    #     [unmappedstatus] => captured
    #     [key] => vd2Y1X
    #     [txnid] => k8WnSppfWj5dO7
    #     [amount] => 10.00
    #     [discount] => 0.00
    #     [net_amount_debit] => 10
    #     [addedon] => 2021-06-18 01:14:54
    #     [productinfo] => iPhone
    #     [firstname] => nishant
    #     [lastname] =>
    #     [address1] =>
    #     [address2] =>
    #     [city] =>
    #     [state] =>
    #     [country] =>
    #     [zipcode] =>
    #     [email] => test@gmail.com
    #     [phone] =>
    #     [udf1] =>
    #     [udf2] =>
    #     [udf3] =>
    #     [udf4] =>
    #     [udf5] =>
    #     [udf6] =>
    #     [udf7] =>
    #     [udf8] =>
    #     [udf9] =>
    #     [udf10] =>
    #     [hash] => e478ad7837422810ff482efca9d8f402fccf4342ad38cb03b23d3311884a1b5dccfecdf135f24a29e815672d2681a5df38d5362b18989d94d8b0ff41d01fb37f
    #     [field1] => 2021-06-18 01:15:16.0
    #     [field2] => 20210618111212800110168941914234127
    #     [field3] => 13297721729
    #     [field4] =>
    #     [field5] =>
    #     [field6] =>
    #     [field7] =>
    #     [field8] =>
    #     [field9] => Txn Success
    #     [payment_source] => payu
    #     [meCode] => {"payee_id":"PayUGo96421738082175","clientId":"C11"}
    #     [PG_TYPE] => CASH-PG
    #     [bank_ref_num] => 20210618111212800110168941914234127
    #     [bankcode] => PAYTM
    #     [error] => E000
    #     [error_Message] => No Error
    # )

# payments/urls.py

from django.urls import path
from .views import payment_list, make_payment
from .views import PaymentList

urlpatterns = [
    path('api/payments/', PaymentList.as_view(), name='payment-list'),
    # Add more URL patterns as needed
    path('payments/', payment_list, name='payment_list'),
    path('make-payment/', make_payment, name='make_payment'),
]

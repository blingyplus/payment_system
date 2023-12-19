# payments/views.py

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Customer, Payment
# payments/views.py

from rest_framework import generics
from .models import Payment
from .serializers import PaymentSerializer

class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payments/payment_list.html', {'payments': payments})

def make_payment(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        customer_email = request.POST.get('customer_email')

        customer, created = Customer.objects.get_or_create(email=customer_email, defaults={'name': 'Anonymous'})

        Payment.objects.create(amount=amount, description=description, customer=customer)

        return JsonResponse({'status': 'success', 'message': 'Payment successful!'})

    return render(request, 'payments/make_payment.html')

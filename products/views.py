from django.shortcuts import render
from products.models import Phone

# Create your views here.


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def phone_view(request):
    if request.method == 'GET':
        products = Phone.objects.all()
        context = {
            'products': products
        }
        return render(request, 'products/phone.html', context=context)

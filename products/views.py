from django.shortcuts import render
from products.models import Phone, Comment

# Create your views here.


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def phones_view(request):
    if request.method == 'GET':
        products = Phone.objects.all()
        context = {
            'products': products
        }
        return render(request, 'products/phone.html', context=context)


def phone_detail_view(request, phone_id):
    if request.method == "GET":
        product = Phone.objects.get(id=phone_id)
        comments = Comment.objects.filter(product=product)

        context = {
            'product': product,
            'comments': comments
        }
        return render(request, 'products/detail.html', context=context)


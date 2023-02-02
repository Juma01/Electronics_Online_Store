from django.shortcuts import render, redirect
from products.models import Phone, Comment
from products.forms import ProductCreateForm, CommentCreateForm

# Create your views here.

PAGINATION_LIMIT = 3


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def phones_view(request):
    if request.method == 'GET':
        products = Phone.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if search:
            products = Phone.objects.filter(
                descriptions__icontains=search
            ) | Phone.objects.filter(
                brand__icontains=search
            )

        """ max page"""
        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        """ slice products by page """
        products = products[PAGINATION_LIMIT * (page-1):PAGINATION_LIMIT * page]

        context = {
            'products': products,
            'user': request.user,
            'max_page': range(1, max_page+1)
        }
        return render(request, 'products/phone.html', context=context)


def phone_detail_view(request, phone_id):
    if request.method == "GET":
        product = Phone.objects.get(id=phone_id)
        comments = Comment.objects.filter(product=product)

        context = {
            'product': product,
            'comments': comments,
            'form': CommentCreateForm,
            'user': request.user
        }
        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        product = Phone.objects.get(id=phone_id)
        comments = Comment.objects.filter(product=product)

        form = CommentCreateForm(data=request.POST)
        if form.is_valid():
            Comment.objects.create(
                author=request.user,
                text=form.cleaned_data.get('text'),
                product=product
            )
            return redirect(f'/products/{product.id}')

        return render(request, 'products/create.html', context={
            'product': product,
            'comments': comments,
            'form': form
        })


def create_product_view(request):
    if request.method == 'GET' and not request.user.is_anonymous:
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)
    elif request.user.is_anonymous:
        return redirect('/products')

    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)

        if form.is_valid():
            Phone.objects.create(
                brand=form.cleaned_data.get('brand'),
                phone_model=form.cleaned_data.get('phone_model'),
                descriptions=form.cleaned_data.get('description'),
                memory=form.cleaned_data.get('memory'),
                color=form.cleaned_data.get('color'),
                price=form.cleaned_data.get('price'),
                rate=form.cleaned_data.get('rate'),
                commentable=form.cleaned_data.get('commentable')
            )
            return redirect('/products')

        return render(request, 'products/create.html', context={
            'form': form
        })

from django.http import Http404
from django.shortcuts import render, redirect

from phones.models import Phone

SORT_REQUEST = {
    'name': 'name',
    'min_price': 'price',
    'max_price': '-price'
}


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()

    sort = request.GET.get('sort')
    if sort:
        phones = phones.order_by(SORT_REQUEST[sort])

    context = {
        'phones': phones
    }

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)

    context = {'phone': phone}
    return render(request, template, context)

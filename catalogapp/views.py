from django.shortcuts import render
from .models import ProductCategory, Product, Promo

# Create your views here.


def main(request):
    title = 'Главная'
    promos = Promo.objects.all()[:]
    context = {'title': title, 'promos': promos}
    return render(request, 'catalogapp/index.html', context=context)


def catalog(request):
    title = 'Общий каталог'
    categories = ProductCategory.objects.all()[:]
    context = {'title': title, 'categories': categories}
    return render(request, 'catalogapp/catalog.html', context=context)


def electonics(request):
    return render(request, 'catalogapp/catalog/electronics.html')


def food(request):
    return render(request, 'catalogapp/catalog/food.html')


def things(request):
    return render(request, 'catalogapp/catalog/things.html')


def contacts(request):
    return render(request, 'catalogapp/contacts.html')

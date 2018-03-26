from django.shortcuts import render
from .models import ProductCategory, Product, Promo

# Create your views here.


def main(request):
    title = 'Главная'
    promos = Promo.objects.all()[:]
    context = {'title': title, 'promos': promos}
    return render(request, 'mainapp/index.html', context=context)


def catalog(request):
    title = 'Общий каталог'
    categories = ProductCategory.objects.all()[:]
    context = {'title': title, 'categories': categories}
    return render(request, 'mainapp/catalog.html', context=context)


def catalog_electonics(request):
    return render(request, 'mainapp/catalog/electronics.html')


def catalog_food(request):
    return render(request, 'mainapp/catalog/food.html')


def catalog_things(request):
    return render(request, 'mainapp/catalog/things.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')

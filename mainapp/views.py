from django.shortcuts import render
from .models import ProductCategory, Product

# Create your views here.


def main(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    title = 'Главная'
    categories = ProductCategory.objects.all()[:]
    content = {'title': title, 'categories': categories}
    return render(request, 'mainapp/catalog.html', content)


def catalog_electonics(request):
    return render(request, 'mainapp/catalog/electronics.html')


def catalog_food(request):
    return render(request, 'mainapp/catalog/food.html')


def catalog_things(request):
    return render(request, 'mainapp/catalog/things.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')

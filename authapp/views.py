from django.http.response import HttpResponseRedirect

from django.shortcuts import render
from django.urls import reverse

from authapp.forms import ShopUserLoginForm
from django.contrib import auth

# Create your views here.


def login(request):
    login_form = ShopUserLoginForm()
    if request.method == "POST":
        login_form = ShopUserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request=request, user=user)
                return HttpResponseRedirect(reverse('main'))
    title = 'Главная'
    context = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    title = 'Главная'
    context = {'title': title}
    return render(request, 'authapp/register.html', context=context)


def edit(request):
    title = 'Редактирование'
    context = {'title': title}
    return render(request, 'authapp/edit.html', context=context)

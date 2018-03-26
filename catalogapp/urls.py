from django.urls import re_path
import catalogapp.views as catalogapp

app_name = 'catalogapp'

urlpatterns = [
    re_path(r'^$', catalogapp.catalog, name='catalog'),
    re_path(r'^electronics', catalogapp.electonics, name='electronics'),
    re_path(r'^food', catalogapp.food, name='food'),
    re_path(r'^things', catalogapp.things, name='things'),
]

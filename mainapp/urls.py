from django.conf.urls import url
import mainapp.views as mainapp


urlpatterns = [
    # url(r'^$', mainapp.catalog, name='main'),
    url(r'^$', mainapp.catalog, name='catalog'),
    url(r'^electronics', mainapp.catalog_electonics, name='electronics'),
    url(r'^food', mainapp.catalog_food, name='food'),
    url(r'^things', mainapp.catalog_things, name='things'),
]

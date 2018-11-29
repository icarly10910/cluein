from django.conf.urls import url
from .views import *

urlpatterns =[
    url(r'^$', index, name='index'), #connects index page to function

    url(r'^display_shirts$', display_shirts, name='display_shirts'),
    url(r'^display_pants$', display_pants, name='display_pants'),
    url(r'^display_shoes$', display_shoes, name='display_shoes'),

    url(r'^add_shirts$', add_shirts, name='add_shirts'),
    url(r'^add_pants$', add_pants, name='add_pants'),
    url(r'^add_shoes$', add_shoes, name='add_shoes')
]
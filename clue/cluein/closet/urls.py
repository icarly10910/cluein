from django.conf.urls import url
from .views import *

urlpatterns =[
    url(r'^$', index, name='index'), #connects index page to function

    url(r'^display_shirts$', display_shirts, name='display_shirts'),
    url(r'^display_pants$', display_pants, name='display_pants'),
    url(r'^display_shoes$', display_shoes, name='display_shoes'),

    url(r'^add_shirts$', add_shirts, name='add_shirts'),
    url(r'^add_pants$', add_pants, name='add_pants'),
    url(r'^add_shoes$', add_shoes, name='add_shoes'),

    url(r'^edit_shirts/(?P<pk>\d+)$', edit_shirts, name="edit_shirts"),
    url(r'^edit_pants/(?P<pk>\d+)$', edit_pants, name="edit_pants"),
    url(r'^edit_shoes/(?P<pk>\d+)$', edit_shoes, name="edit_shoes"),

    url(r'^delete_shirts/(?P<pk>\d+)$', delete_shirts, name="delete_shirts"),
    url(r'^delete_pants/(?P<pk>\d+)$', delete_pants, name="delete_pants"),
    url(r'^delete_shoes/(?P<pk>\d+)$', delete_shoes, name="delete_shoes")
]

from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^(?P<good_id>\d+)$', good_page, name='good_page'),
    url(r'^add(?P<good_id>\d+)$', add_to_cart, name='add_to_cart'),
    url(r'^buy$', buy_goods, name='buy_goods'),
    url(r'^search$', search, name='search'),
]

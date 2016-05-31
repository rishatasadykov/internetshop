from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^catalog$', CatalogView.as_view(), name='catalog'),
    url(r'^$', main, name='main'),
    url(r'^register$', register, name='register'),
    url(r'^feedback$', feedback, name='feedback'),
]

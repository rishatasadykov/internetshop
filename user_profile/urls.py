from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', user_profile, name='user_profile'),
    url(r'^edit(?P<user_id>\d+)$', edit_user_profile, name='edit_user_profile'),
    url(r'^top_up\d+$', top_up, name='top_up'),
    url(r'^change_avatar$', change_avatar, name='change_avatar'),
]
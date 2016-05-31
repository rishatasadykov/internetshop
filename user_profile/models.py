from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


currencies = (
    ("USD", "USD"),
    ("EUR", "EURO"),
    ("RUB", "RUBLES"),
)


def get_user_image_path(instance, filename):
        return "%s\\%s" % (instance.user.username,  filename)


class UserProfile(models.Model):
    class Meta:
        db_table = "userprofiles"

    user = models.ForeignKey(User)
    balance = models.IntegerField(default=0)
    currency = models.CharField(choices=currencies, max_length=3)
    avatar = models.ImageField(upload_to=get_user_image_path, blank=True, null=True)
    site = models.URLField(blank=True)

    def __unicode__(self):
        return unicode(self.user)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance', 'currency', 'avatar', 'site')
    list_filter = ('user', 'balance', 'currency', 'avatar', 'site')


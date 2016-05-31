from django.db import models
from django.contrib import admin
from user_profile.models import UserProfile


class Feedback(models.Model):
    class Meta:
        db_table = "feedbacks"

    user = models.ForeignKey(UserProfile)
    message = models.TextField(max_length=1000)

    def __unicode__(self):
        return unicode(self.user)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'message')
    list_filter = ('user', 'message')
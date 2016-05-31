from django.contrib import admin
from models import *

admin.site.register(Good, GoodAdmin)
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Cart, CartAdmin)
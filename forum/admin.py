from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ForumPost, Like, Comments


admin.site.register(ForumPost)
admin.site.register(Like)
admin.site.register(Comments)
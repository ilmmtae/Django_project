from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, FriendRequest, Group, Like, Comment, Post

# Register your models here.


admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Group)
admin.site.register(FriendRequest)
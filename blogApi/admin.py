from django.contrib import admin
from .models import Post, Category, Likes, Profile, Comments

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Likes)
admin.site.register(Comments)
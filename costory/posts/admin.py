from django.contrib import admin

from posts.models import Post
from .models import Post

# Register your models here.
admin.site.register(Post)
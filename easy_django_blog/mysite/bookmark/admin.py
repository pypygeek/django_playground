from django.contrib import admin
from bookmark.models import Bookmark

# Register your models here.
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')

# 데코레이터 없이 사용할 경우 직접 등록 해줘야함.    
# admin.site.register(Bookmark, BookmarkAdmin)
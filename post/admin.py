from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'author', 'date_created']
    search_fields = ['title']
    list_filter = ['title', 'author', 'date_created']
    ordering = ['date_created']


admin.site.register(Post, PostAdmin)

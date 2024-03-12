from django.contrib import admin
from .models import Post, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status'] # атрибуты полей, которые надо вывести
    list_filter = ['status', 'created', 'publish', 'author'] # фильтр, правая боковая панель
    search_fields = ['title', 'body'] # поиск по имени поста и содержимого
    prepopulated_fields = {'slug': ('title',)} #автозаполнение слага по тайтл
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish'] #сортировка по умолчанию



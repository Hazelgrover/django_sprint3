from django.contrib import admin
from django.db import models
from .models import Post, Category, Location


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author', 'category', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('title',)
    list_filter = ('category', 'is_published')
    fieldsets = (
        (None, {
            'fields': ('title', 'text', 'pub_date', 'author', 'category',
                       'location', 'is_published')
        }),
    )
    formfield_overrides = {
        models.BooleanField: {
            'help_text': 'Снимите галочку, чтобы скрыть публикацию.'
        },
        models.SlugField: {
            'help_text': ('Идентификатор страницы для URL; разрешены символы '
                          'латиницы, цифры, дефис и подчёркивание.')
        },
        models.DateTimeField: {
            'help_text': ('Если установить дату и время в будущем — можно '
                          'делать отложенные публикации.')
        },
    }


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('title',)
    list_filter = ('is_published',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'slug', 'is_published')
        }),
    )
    formfield_overrides = {
        models.BooleanField: {
            'help_text': 'Снимите галочку, чтобы скрыть публикацию.'
        },
        models.SlugField: {
            'help_text': ('Идентификатор страницы для URL; разрешены символы '
                          'латиницы, цифры, дефис и подчёркивание.')
        },
    }


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_filter = ('is_published',)
    fieldsets = (
        (None, {
            'fields': ('name', 'is_published')
        }),
    )
    formfield_overrides = {
        models.BooleanField: {
            'help_text': 'Снимите галочку, чтобы скрыть публикацию.'
        },
    }


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)

admin.site.site_title = 'Блог'
admin.site.site_header = 'Блог'

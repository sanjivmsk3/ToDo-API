import imp
from django.contrib import admin
from app.models import TodoItem

# Register your models here.
@admin.register(TodoItem)
class TodoAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'created', 'updated')
    list_display_links = ('title', 'author',)
    list_filter = ('author', 'created', 'updated',)
    search_fields = ['title', 'author',]
 
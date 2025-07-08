from django.contrib import admin
from .models import Task, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'priority', 'is_completed', 'created_at')
    list_filter = ('is_completed', 'category', 'priority', 'created_at')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'
    ordering = ('-priority', '-created_at')
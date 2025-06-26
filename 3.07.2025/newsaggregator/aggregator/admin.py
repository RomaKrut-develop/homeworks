from django.contrib import admin
from .models import NewsSource, NewsItem

@admin.register(NewsSource)
class NewsSourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'active')
    list_editable = ('active',)

@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'published_at')
    list_filter = ('source', 'published_at')
    search_fields = ('title',)

admin.site.site_header = "News Aggregator Admin"
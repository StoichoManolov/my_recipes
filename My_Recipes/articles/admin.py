from django.contrib import admin

from My_Recipes.articles.models import Article


# Register your models here.
@admin.register(Article)
class ArticleAdminForm(admin.ModelAdmin):
    list_display = ('category', 'title', 'created_at')
    ordering = ('created_at',)
    list_filter = ['category', 'title', ]
    search_fields = ('category', 'title',)
    fieldsets = (
        ('Main Information', {
            'fields': ('category', 'created_at'),
        }),
        ('Title', {
            'fields': ('title',),
        }),
        ('Rest of article', {
            'fields': ('description', 'content', )
        })
    )
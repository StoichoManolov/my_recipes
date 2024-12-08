from django.contrib import admin

from My_Recipes.articles.models import Article


# Register your models here.
@admin.register(Article)
class ArticleAdminForm(admin.ModelAdmin):

    list_display = ('category', 'title', 'created_at', 'created_by')
    ordering = ('title', 'category', 'created_at', 'created_by')
    list_filter = ['category', 'title', 'created_at', 'created_by']
    search_fields = ('category', 'title', 'created_by')
    fieldsets = (
        ('Main Information', {
            'fields': ('category', 'title', 'created_by'),
        }),
        ('Rest of article', {
            'fields': ('description', 'content', )
        })
    )
    readonly_fields = ['created_at']
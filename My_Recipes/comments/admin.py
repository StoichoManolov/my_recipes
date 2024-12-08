from django.contrib import admin

from My_Recipes.comments.models import RecipeComment, ArticleComment


# Register your models here.


@admin.register(RecipeComment)
class RecipeCommentAdminForm(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at', 'recipe')
    ordering = ('user', 'content', 'created_at', 'recipe')
    list_filter = ('user', 'content', 'created_at', 'recipe')
    search_fields = ('user', 'content', 'created_at', 'recipe')
    fieldsets = (
        ('Main Information', {
            'fields': ('user', 'created_at', 'recipe'),
        }),
        ('Comment Content', {
            'fields': ('content',)
        }),
    )
    readonly_fields = ['created_at']


@admin.register(ArticleComment)
class ArticleCommentAdminForm(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at', 'article')
    ordering = ('user', 'content', 'created_at', 'article')
    list_filter = ('user', 'content', 'created_at', 'article')
    search_fields = ('user', 'content', 'created_at', 'article')
    fieldsets = (
        ('Main Information', {
            'fields': ('user', 'created_at', 'article'),
        }),
        ('Comment Content', {
            'fields': ('content',)
        }),
    )
    readonly_fields = ['created_at']

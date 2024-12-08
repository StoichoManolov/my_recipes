from django.contrib import admin

from My_Recipes.reviews.models import RecipeReview, ArticleReview


# Register your models here.
@admin.register(RecipeReview)
class RecipeReviewAdminForm(admin.ModelAdmin):

    list_display = ('user', 'rating', 'recipe', 'created_at',)
    list_filter = ('user', 'created_at', 'recipe', 'rating')
    ordering = ('created_at', 'user', 'rating', 'recipe')
    search_fields = ('user', 'recipe')
    fieldsets = (
        ('Main Information', {
            'fields': ('user', 'created_at'),
        }),
        ('Rating', {
            'fields': ('rating',)
        }),
        ('Recipe', {
            'fields': ('recipe', )
        })
    )
    readonly_fields = ['created_at', ]


@admin.register(ArticleReview)
class ArticleReviewAdminForm(admin.ModelAdmin):

    list_display = ('user', 'rating', 'article', 'created_at',)
    list_filter = ('user', 'created_at', 'article', 'rating')
    ordering = ('created_at', 'user', 'rating', 'article')
    search_fields = ('user', 'article')
    fieldsets = (
        ('Main Information', {
            'fields': ('user', 'created_at'),
        }),
        ('Rating', {
            'fields': ('rating',)
        }),
        ('Article', {
            'fields': ('article', )
        })
    )
    readonly_fields = ['created_at', ]


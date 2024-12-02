from django.contrib import admin

from My_Recipes.recipe_ingredients.models import RecipesIngredient


# Register your models here.
@admin.register(RecipesIngredient)
class RecipesIngredientAdminForm(admin.ModelAdmin):

    list_display = ('recipe', 'ingredient', 'quantity', 'measurement',)
    ordering = ('recipe', 'ingredient', 'quantity', 'measurement',)
    list_filter = ('recipe', 'ingredient', 'quantity', 'measurement',)
    search_fields = ('recipe', 'ingredient', 'quantity', 'measurement',)
    fieldsets = (
        ('Recipe', {
            'fields': ('recipe',),
        }),
        ('Ingredients', {
            'fields': ('ingredient','quantity', 'measurement',)
        }),
    )
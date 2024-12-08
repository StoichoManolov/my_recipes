from django.contrib import admin

from My_Recipes.recipe_ingredients.models import RecipesIngredient
from My_Recipes.recipes.models import Recipe


# Register your models here.

class RecipesIngredientInline(admin.TabularInline):  # Use TabularInline or StackedInline
    model = RecipesIngredient
    extra = 1
    fields = ('ingredient', 'quantity', 'measurement')  # Fields for each inline form


@admin.register(Recipe)
class RecipeAdminForm(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'created_by', 'cook_time', 'prep_time', 'total_time')
    ordering = ('title', 'prep_time', 'cook_time', 'created_at', 'created_by',)
    list_filter = ['prep_time', 'cook_time', 'title', 'created_at', 'created_by']
    search_fields = ('title', 'created_by', 'cook_time', 'prep_time')
    inlines = [RecipesIngredientInline]
    fieldsets = (
        ('Main Information', {
            'fields': ('title', 'created_by', 'created_at'),
        }),
        ('Cooking Time', {
            'fields': ('prep_time', 'cook_time',)
        }),
        ('Rest of article', {
            'fields': ('description', 'instructions',)
        })
    )
    readonly_fields = ['created_at']

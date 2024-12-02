from django.contrib import admin

from My_Recipes.ingredients.models import Ingredients


# Register your models here.
@admin.register(Ingredients)
class IngredientAdminForm(admin.ModelAdmin):

    list_display = ('name',)
    list_filter = ('name', )
    ordering = ('name', )
    search_fields = ('name', )
    fieldsets = (
        ('Ingredient Name', {
            'fields': ('name', ),
        }),
    )


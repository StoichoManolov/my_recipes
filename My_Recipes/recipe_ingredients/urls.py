from django.urls import path

from My_Recipes.recipe_ingredients.views import IngredientListView, CreateIngredientView, DeleteIngredientView, \
    EditIngredientView

urlpatterns = [
    path('recipe/<int:recipe_id>/manage-ingredients/', IngredientListView.as_view(), name='manage-ingredients'),
    path('recipe/<int:recipe_id>/ingredients/create/', CreateIngredientView.as_view(), name='ingredient-create'),
    path('recipe/<int:recipe_id>/ingredients/<int:ingredient_id>/edit/',
         EditIngredientView.as_view(), name='ingredient-edit'),
    path('recipe/<int:recipe_id>/ingredients/<int:ingredient_id>/delete/',
         DeleteIngredientView.as_view(), name='ingredient-delete'),
]


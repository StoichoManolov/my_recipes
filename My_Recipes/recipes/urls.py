from django.urls import path, include

from My_Recipes.recipes.views import RecipeListView, RecipeDetailView, DeleteRecipeView, EditRecipeView, \
    CreateRecipeView

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list'),
    path('create/', CreateRecipeView.as_view(), name='recipe-create'),
    path('<int:pk>/', include([
        path('detail/', RecipeDetailView.as_view(), name='recipe-detail'),
        path('delete/', DeleteRecipeView.as_view(), name='recipe-delete'),
        path('edit/', EditRecipeView.as_view(), name='recipe-edit'),
    ])),
]
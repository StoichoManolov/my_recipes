from django.urls import path
from My_Recipes.reviews.views import SubmitRecipeReviewView, SubmitArticleReviewView

urlpatterns = [
    path('recipe/<int:recipe_id>/submit_review/', SubmitRecipeReviewView.as_view(), name='submit_recipe_review'),
    path('article/<int:article_id>/submit_review/', SubmitArticleReviewView.as_view(), name='submit_article_review'),
]

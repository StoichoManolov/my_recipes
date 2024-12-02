from django import forms

from My_Recipes.reviews.models import RecipeReview, ArticleReview


class RecipeReviewForm(forms.ModelForm):
    class Meta:
        model = RecipeReview
        fields = ['rating']


class ArticleReviewForm(forms.ModelForm):
    class Meta:
        model = ArticleReview
        fields = ['rating']


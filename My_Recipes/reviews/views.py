from django.shortcuts import get_object_or_404, redirect
from django.views.generic import FormView

from My_Recipes.articles.models import Article
from My_Recipes.recipes.models import Recipe
from My_Recipes.reviews.forms import RecipeReviewForm, ArticleReviewForm
from My_Recipes.reviews.models import RecipeReview, ArticleReview


class SubmitRecipeReviewView(FormView):
    template_name = 'recipes/detail-recipe.html'
    form_class = RecipeReviewForm

    def get_recipe(self):
        return get_object_or_404(Recipe, pk=self.kwargs['recipe_id'])

    def form_valid(self, form):
        recipe = self.get_recipe()

        RecipeReview.objects.create(
            recipe=recipe,
            user=self.request.user,
            rating=form.cleaned_data['rating']
        )
        return redirect('recipe-detail', pk=recipe.id)


class SubmitArticleReviewView(FormView):
    template_name = 'articles/detail-article.html'
    form_class = ArticleReviewForm

    def get_article(self):
        return get_object_or_404(Article, pk=self.kwargs['article_id'])

    def form_valid(self, form):
        article = self.get_article()

        # Save the review
        ArticleReview.objects.create(
            article=article,
            user=self.request.user,
            rating=form.cleaned_data['rating']
        )
        return redirect('article-detail', pk=article.id)



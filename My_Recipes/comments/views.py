from django.core.exceptions import PermissionDenied
from django.http import JsonResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView

from .mixins import CheckForRestrictionRecipes
from .models import RecipeComment, ArticleComment
from .forms import CommentForm, ArticleCommentForm
from ..articles.models import Article
from ..recipes.models import Recipe


class RecipeCommentCreateView(CreateView):
    model = RecipeComment
    form_class = CommentForm
    template_name = 'recipes/detail-recipe.html'

    def form_valid(self, form):
        recipe_id = self.kwargs['recipe_id']
        recipe = get_object_or_404(Recipe, id=recipe_id)

        # Associate the comment with the current user and recipe
        form.instance.recipe = recipe
        form.instance.user = self.request.user
        form.save()

        # After saving the comment, redirect to the recipe detail page (this will reload with the new comment)
        return redirect('recipe-detail', pk=recipe.id)

    def form_invalid(self, form):
        # If form is invalid, render the page with form errors
        return self.render_to_response({'form': form, 'recipe': self.get_object()})


class RecipeCommentDeleteView(View):
    def post(self, request, pk):
        comment = get_object_or_404(RecipeComment, pk=pk)

        # Check if the user is the owner of the comment or has permission to delete (superuser/admin)
        if comment.user == request.user or request.user.is_superuser:
            recipe_id = comment.recipe.pk  # Get the associated recipe ID
            comment.delete()
            return redirect('recipe-detail', pk=recipe_id)  # Redirect to the recipe's detail page

        return HttpResponseForbidden('You do not have permission to delete this comment.')


class RecipeCommentUpdateView(CheckForRestrictionRecipes, UpdateView):
    model = RecipeComment
    form_class = CommentForm
    template_name = 'comments/update-comment.html'

    def form_valid(self, form):
        comment = self.get_object()  # Get the current comment instance

        # Ensure the current user is the owner of the comment or a superuser
        if comment.user == self.request.user or self.request.user.is_superuser or self.request.user.is_staff:
            form.save()  # Save the updated comment
            return redirect('recipe-detail', pk=comment.recipe.pk)  # Redirect to the recipe detail page
        else:
            return redirect('recipe-detail', pk=comment.recipe.pk)  # Redirect if unauthorized

    def form_invalid(self, form):
        # Handle invalid form submission
        return super().form_invalid(form)


class ArticleCreateView(CreateView):
    model = ArticleComment
    form_class = ArticleCommentForm
    template_name = 'articles/detail-article.html'

    def form_valid(self, form):
        article = get_object_or_404(Article, id=self.kwargs['article_id'])
        form.instance.article = article
        form.instance.user = self.request.user

        # Save the form and redirect to the article detail view
        form.save()
        return redirect('article-detail', pk=article.id)

    def form_invalid(self, form):
        # If form is invalid, render the page with form errors
        return self.render_to_response({'form': form, 'article': self.get_object()})


class ArticleDeleteView(View):
    def post(self, request, pk):
        comment = get_object_or_404(ArticleComment, pk=pk)

        # Check if the user is the owner of the comment or has permission to delete (superuser/admin)
        if comment.user == request.user or request.user.is_superuser:
            article_id = comment.article.pk  # Get the associated recipe ID
            comment.delete()
            return redirect('article-detail', pk=article_id)  # Redirect to the recipe's detail page

        return HttpResponseForbidden('You do not have permission to delete this comment.')


class ArticleUpdateView(CheckForRestrictionRecipes, UpdateView):
    model = ArticleComment
    form_class = ArticleCommentForm
    template_name = 'comments/update-comment.html'

    def form_valid(self, form):
        comment = self.get_object()  # Get the current comment instance

        # Ensure the current user is the owner of the comment or a superuser
        if comment.user == self.request.user or self.request.user.is_superuser or self.request.user.is_staff:
            form.save()  # Save the updated comment
            return redirect('article-detail', pk=comment.article.pk)  # Redirect to the recipe detail page
        else:
            return redirect('article-detail', pk=comment.article.pk)  # Redirect if unauthorized

    def form_invalid(self, form):
        # Handle invalid form submission
        return super().form_invalid(form)
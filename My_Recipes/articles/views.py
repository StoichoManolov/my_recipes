from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from My_Recipes.accounts.models import RecipesUser
from My_Recipes.articles.forms import ArticleForm
from My_Recipes.articles.mixins import CheckUserArticlePermission
from My_Recipes.articles.models import Article
from My_Recipes.reviews.models import ArticleReview


# Create your views here.
class CreateArticleView(CheckUserArticlePermission, CreateView):

    model = Article
    form_class = ArticleForm
    template_name = 'articles/create-article.html'
    success_url = reverse_lazy('articles-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ArticleDetailView(DetailView):

    template_name = 'articles/detail-article.html'
    model = Article

    def get_user(self):
        return get_object_or_404(RecipesUser, pk=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.object
        avg_rating = article.get_average_rating() if article.get_average_rating() is not None else 0
        reviews_count = article.reviews_count()

        if self.request.user.is_authenticated:
            user = ArticleReview.objects.filter(article=article, user=self.request.user).first()

            context['user_review'] = user
        context['article'] = article
        context['avg_rating'] = avg_rating
        context['reviews_count'] = reviews_count

        return context


class DeleteArticleView(CheckUserArticlePermission, DeleteView):

    model = Article
    success_url = reverse_lazy('articles-list')
    template_name = 'articles/delete-article.html'


class EditArticleView(CheckUserArticlePermission, UpdateView):

    model = Article
    form_class = ArticleForm
    template_name = 'articles/edit-article.html'
    success_url = reverse_lazy('articles-list')


class ArticlesListView(ListView):

    template_name = 'articles/list-articles.html'
    model = Article
    context_object_name = 'articles'

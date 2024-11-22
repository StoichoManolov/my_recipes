from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from My_Recipes.articles.forms import ArticleForm
from My_Recipes.articles.mixins import CheckUserArticlePermission
from My_Recipes.articles.models import Article


# Create your views here.
class CreateArticleView(CheckUserArticlePermission, CreateView):

    model = Article
    form_class = ArticleForm
    template_name = 'articles/create-article.html'
    success_url = reverse_lazy('articles-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleDetailView(DetailView):

    template_name = 'articles/detail-article.html'
    model = Article


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

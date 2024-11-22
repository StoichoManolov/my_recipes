from django import forms

from My_Recipes.articles.models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ['created_at', 'updated_at', 'author',]
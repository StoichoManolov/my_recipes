from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import TemplateView

from My_Recipes.articles.models import Article
from My_Recipes.recipes.models import Recipe


# Create your views here.
UserModel = get_user_model()


class Homepage(TemplateView):

    template_name = 'common/front_page.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['recipes'] = Recipe.objects.all().count()
        data['articles'] = Article.objects.all().count()
        data['registered_users'] = UserModel.objects.all().count()

        return data
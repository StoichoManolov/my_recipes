from django.urls import path, include

from My_Recipes.articles.views import CreateArticleView, ArticlesListView, ArticleDetailView, DeleteArticleView, \
    EditArticleView

urlpatterns = [
    path('create/', CreateArticleView.as_view(), name='create-article'),
    path('', ArticlesListView.as_view(), name='articles-list'),
    path('<int:pk>/', include([
        path('detail/', ArticleDetailView.as_view(), name='article-detail'),
        path('delete/', DeleteArticleView.as_view(), name='article-delete'),
        path('edit/', EditArticleView.as_view(), name='article-edit'),
    ])),
]

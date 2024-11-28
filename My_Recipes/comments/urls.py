from django.urls import path

from My_Recipes.comments.views import RecipeCommentCreateView, RecipeCommentDeleteView, RecipeCommentUpdateView, \
    ArticleCreateView, ArticleDeleteView, ArticleUpdateView

urlpatterns = [
    path('recipe/<int:recipe_id>/comment/', RecipeCommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/delete/', RecipeCommentDeleteView.as_view(), name='comment-delete'),
    path('comment/<int:pk>/update/', RecipeCommentUpdateView.as_view(), name='comment-update'),
    path('article/<int:article_id>/comment/', ArticleCreateView.as_view(), name='comment-article-create'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='comment-article-delete'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='comment-article-update'),
]

from django.db import models

from My_Recipes.accounts.models import RecipesUser
from My_Recipes.articles.models import Article
from My_Recipes.recipes.models import Recipe


# Create your models here.

class CommentBase(models.Model):
    user = models.ForeignKey(RecipesUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class RecipeComment(CommentBase):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"Comment by {self.user.email} on {self.recipe.title}"


class ArticleComment(CommentBase):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"Comment by {self.user.email} on {self.article.title}"

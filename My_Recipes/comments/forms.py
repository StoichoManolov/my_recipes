from django import forms

from My_Recipes.comments.models import RecipeComment, ArticleComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = RecipeComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Enter your comment...',
                'class': 'disabled-textarea',
                'rows': 8,
            }),
        }


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Enter your comment...',
                'class': 'disabled-textarea',
                'rows': 8,
            }),
        }

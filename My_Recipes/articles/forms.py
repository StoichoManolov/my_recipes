from django import forms

from My_Recipes.articles.models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ['created_at', 'created_by',]

        widgets = {
            'description': forms.Textarea(attrs={
                'cols': 40,
                'rows': 4,
                'class': 'disabled-textarea',
                'placeholder': 'Enter a brief description...',
            }),
            'category': forms.TextInput(attrs={
                'placeholder': 'Enter a category...'
            }),
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter a title...'
            })
        }

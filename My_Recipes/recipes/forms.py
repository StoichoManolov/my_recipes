from django import forms

from My_Recipes.recipes.models import Recipe


class RecipeForms(forms.ModelForm):

    class Meta:
        model = Recipe
        exclude = ['created_at', 'created_by', ]

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter the recipe title',
                'class': 'form-control',
            }),
            'category': forms.TextInput(attrs={
                'placeholder': 'Enter the category (e.g., News, Tech)',
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter a brief description',
                'class': 'form-control',
                'rows': 3,
            }),
            'instructions': forms.Textarea(attrs={
                'placeholder': 'Write instructions for cooking..',
                'class': 'form-control',
                'rows': 10,
            }),
        }
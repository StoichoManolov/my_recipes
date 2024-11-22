from django import forms

from My_Recipes.recipes.models import Recipe


class RecipeForms(forms.ModelForm):

    class Meta:
        model = Recipe
        exclude = ['created_at', 'created_by', ]

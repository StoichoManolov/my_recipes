from django import forms
from django.core.exceptions import ValidationError

from My_Recipes.ingredients.models import Ingredients
from My_Recipes.recipe_ingredients.models import RecipesIngredient


class RecipesIngredientForm(forms.ModelForm):

    ingredient_name = forms.CharField(max_length=15, label='Ingredient', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = RecipesIngredient
        fields = ['ingredient_name', 'quantity', 'measurement']
        widgets = {
            'ingredient_name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 6}),
            'measurement': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 20}),
        }

    def clean_ingredient_name(self):
        ingredient_name = self.cleaned_data['ingredient_name']
        # Check that ingredient_name contains only letters and spaces
        if not ingredient_name.isalpha() and not all(char.isalpha() or char.isspace() for char in ingredient_name):
            raise ValidationError('Ingredient name must only contain letters and spaces.')
        return ingredient_name

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        # Check that quantity contains only numbers
        if not quantity.isdigit():
            raise ValidationError('Quantity must be a number.')
        return quantity

    def clean(self):
        cleaned_data = super().clean()
        # Add additional form-wide validation if needed
        return cleaned_data

    def save(self, commit=True):
        # Get the ingredient from the provided name
        ingredient_name = self.cleaned_data.get('ingredient_name')

        # Try to get the existing ingredient or create a new one
        ingredient, created = Ingredients.objects.get_or_create(name=ingredient_name)

        # Create the RecipesIngredient object, associating it with the found or newly created ingredient
        recipe_ingredient = super().save(commit=False)
        recipe_ingredient.ingredient = ingredient  # Assign the correct ingredient to this recipe ingredient

        if commit:
            recipe_ingredient.save()

        return recipe_ingredient


class EditIngredientForm(RecipesIngredientForm):

    def __init__(self, *args, **kwargs):
        # Pass the instance (RecipesIngredient) so we can pre-populate the ingredient name
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.ingredient:
            # Initialize ingredient_name field with the current ingredient's name
            self.fields['ingredient_name'].initial = self.instance.ingredient.name



from django import forms

from My_Recipes.ingredients.models import Ingredients
from My_Recipes.recipe_ingredients.models import RecipesIngredient


class RecipesIngredientForm(forms.ModelForm):

    ingredient_name = forms.CharField(max_length=30, label='Ingredient', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = RecipesIngredient
        fields = ['ingredient_name', 'quantity', 'measurement']
        widgets = {
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'measurement': forms.TextInput(attrs={'class': 'form-control'}),
        }

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



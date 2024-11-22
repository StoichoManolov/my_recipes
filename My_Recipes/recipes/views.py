from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

from My_Recipes.ingredients.models import Ingredients
from My_Recipes.recipe_ingredients.models import RecipesIngredient
from My_Recipes.recipes.forms import RecipeForms
from My_Recipes.recipes.mixins import CheckForRestrictionRecipes, NotApprovedContent
from My_Recipes.recipes.models import Recipe


# Create your views here.

class CreateRecipeView(LoginRequiredMixin, CreateView):

    model = Recipe
    form_class = RecipeForms
    template_name = 'recipes/create-recipe.html'
    success_url = reverse_lazy('recipe-list')

    def form_valid(self, form):

        # Handle the dynamic ingredients
        ingredient_names = self.request.POST.getlist('ingredient_name[]')
        ingredient_quantities = self.request.POST.getlist('ingredient_quantity[]')
        ingredient_measurements = self.request.POST.getlist('ingredient_measurement[]')

        for idx, (name, quantity, measurement) in enumerate(
                zip(ingredient_names, ingredient_quantities, ingredient_measurements)):
            if not name and not quantity and not measurement:
                form.add_error(None, f'Make sure to fill Ingredients, Quantity and Measurement!')
                return self.form_invalid(form)
            elif not name:
                form.add_error(None, f'Make sure to fill ingredients!')
                return self.form_invalid(form)
            elif not quantity:
                form.add_error(None, f'Make sure to fill the quantity of the ingredient!')
                return self.form_invalid(form)
            elif not measurement:
                form.add_error(None, f'Make sure to fill the measurement!')
                return self.form_invalid(form)  # Return to the form with error

        # Save the recipe first (without committing to the database yet)
        recipe = form.save(commit=False)
        recipe.created_by = self.request.user  # Set the current user as the creator
        recipe.save()

        # Create or get the ingredient object
        ingredient, created = Ingredients.objects.get_or_create(name=name)

        # Create the RecipeIngredient to associate the ingredient with the recipe
        RecipesIngredient.objects.create(
            recipe=recipe,
            ingredient=ingredient,
            quantity=quantity,
            measurement=measurement
        )

    # If validation passes, redirect to the success URL
        return redirect(self.success_url)


class RecipeDetailView(DetailView):

    template_name = 'recipes/detail-recipe.html'
    model = Recipe


class DeleteRecipeView(CheckForRestrictionRecipes, LoginRequiredMixin, DeleteView):

    model = Recipe
    success_url = reverse_lazy('recipe-list')
    template_name = 'recipes/delete-recipe.html'


class EditRecipeView(CheckForRestrictionRecipes, LoginRequiredMixin, UpdateView):

    model = Recipe
    form_class = RecipeForms
    template_name = 'recipes/edit-recipe.html'
    success_url = reverse_lazy('recipe-list')


class RecipeListView(ListView):

    template_name = 'recipes/list-recipe.html'
    model = Recipe
    context_object_name = 'recipes'

class NotApproveRecipes(NotApprovedContent, ListView):

    model = Recipe

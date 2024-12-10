import re

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

from My_Recipes.accounts.models import RecipesUser
from My_Recipes.ingredients.models import Ingredients
from My_Recipes.recipe_ingredients.models import RecipesIngredient
from My_Recipes.recipes.forms import RecipeForms
from My_Recipes.recipes.mixins import CheckForRestrictionRecipes
from My_Recipes.recipes.models import Recipe
from My_Recipes.reviews.models import RecipeReview


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
                form.add_error(None, f'Make sure to fill Ingredients, Quantity, and Measurement!')
                return self.form_invalid(form)
            elif not name or len(name.strip()) <= 2 or not re.match(r'^[A-Za-z\s]+$', name.strip()) or len(name) > 15:
                form.add_error(None, "Make sure Ingredient name has:")
                form.add_error(None, "At least 3 characters!")
                form.add_error(None, 'No more than 15 characters!')
                form.add_error(None, "Only letters, no special characters or numbers!")
                return self.form_invalid(form)
            elif not quantity or not quantity.isdigit() or len(quantity) > 6:
                form.add_error(None, "Make sure Ingredient quantity has:")
                form.add_error(None, 'No more than 6 digits!')
                form.add_error(None, "Only digits!")
                return self.form_invalid(form)
            elif not measurement or len(measurement) > 20 or not re.match(r'^[A-Za-z\s\'\-]+$', measurement.strip()):
                form.add_error(None, "Make sure Ingredient measurement has:")
                form.add_error(None, 'No more than 20 characters!')
                form.add_error(None, "Only letters!")
                return self.form_invalid(form)

        # Save the recipe first (without committing to the database yet)
        recipe = form.save(commit=False)
        recipe.created_by = self.request.user  # Set the current user as the creator
        recipe.save()

        # Iterate through the ingredients and save them in the RecipeIngredient model
        for name, quantity, measurement in zip(ingredient_names, ingredient_quantities, ingredient_measurements):
            # Create or get the ingredient object
            ingredient, created = Ingredients.objects.get_or_create(name=name)

            # Create the RecipeIngredient to associate the ingredient with the recipe
            RecipesIngredient.objects.create(
                recipe=recipe,
                ingredient=ingredient,
                quantity=quantity,
                measurement=measurement
            )

        return redirect(self.success_url)


class RecipeDetailView(DetailView):
    template_name = 'recipes/detail-recipe.html'
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.object
        avg_rating = recipe.get_average_rating()
        reviews_count = recipe.reviews_count()

        if self.request.user.is_authenticated:
            user = RecipeReview.objects.filter(recipe=recipe, user=self.request.user).first()

            context['user_review'] = user

        context['recipe'] = recipe
        context['avg_rating'] = avg_rating
        context['reviews_count'] = reviews_count

        return context


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


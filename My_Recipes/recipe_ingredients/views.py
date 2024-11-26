from django.contrib import messages
from django.http import Http404
from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from My_Recipes.recipe_ingredients.forms import RecipesIngredientForm, EditIngredientForm
from My_Recipes.recipe_ingredients.mixins import CheckForRestrictionIngredients
from My_Recipes.recipe_ingredients.models import RecipesIngredient
from My_Recipes.recipes.models import Recipe


class IngredientListView(CheckForRestrictionIngredients, ListView):
    model = RecipesIngredient
    template_name = 'ingredients/manage-ingredients.html'
    context_object_name = 'ingredients'

    def get_queryset(self):
        recipe_id = self.kwargs['recipe_id']
        return RecipesIngredient.objects.filter(recipe_id=recipe_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = get_object_or_404(Recipe, pk=self.kwargs['recipe_id'])
        return context


class CreateIngredientView(CheckForRestrictionIngredients, CreateView):
    model = RecipesIngredient
    form_class = RecipesIngredientForm
    template_name = 'ingredients/create-ingredient.html'

    def form_valid(self, form):
        # Associate the ingredient with the correct recipe
        recipe = get_object_or_404(Recipe, id=self.kwargs['recipe_id'])
        form.instance.recipe = recipe
        return super().form_valid(form)

    def get_success_url(self):
        recipe_id = self.kwargs['recipe_id']
        return reverse_lazy('manage-ingredients', kwargs={'recipe_id': recipe_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the recipe to the context for template access
        context['recipe'] = get_object_or_404(Recipe, pk=self.kwargs['recipe_id'])
        return context


class DeleteIngredientView(CheckForRestrictionIngredients, DeleteView):
    model = RecipesIngredient
    template_name = 'ingredients/delete-ingredient.html'

    def get_object(self):
        ingredient_id = self.kwargs['ingredient_id']
        recipe_id = self.kwargs['recipe_id']
        ingredient = RecipesIngredient.objects.filter(id=ingredient_id, recipe_id=recipe_id).first()
        if not ingredient:
            raise Http404("Ingredient not found")
        return ingredient

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ingredient = self.get_object()  # Get the ingredient object
        recipe = ingredient.recipe  # Get the recipe associated with this ingredient
        # Add a flag to the context that indicates if the recipe has only one ingredient left
        context['is_last_ingredient'] = recipe.recipe_ingredients.count() == 1
        context['recipe'] = recipe  # Pass the recipe object so its ID can be used in the URL
        return context

    def delete(self, request, *args, **kwargs):
        ingredient = self.get_object()
        recipe = ingredient.recipe

        if recipe.recipe_ingredients.count() == 1:
            messages.error(request, "You cannot delete the last ingredient in a recipe.")
            return redirect(reverse_lazy('manage-ingredients', kwargs={'recipe_id': recipe.id}))

        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        recipe_id = self.kwargs['recipe_id']
        return reverse_lazy('manage-ingredients', kwargs={'recipe_id': recipe_id})

class EditIngredientView(CheckForRestrictionIngredients, UpdateView):
    model = RecipesIngredient
    template_name = 'ingredients/edit-ingredient.html'
    form_class = EditIngredientForm

    def get_object(self):
        ingredient_id = self.kwargs['ingredient_id']
        recipe_id = self.kwargs['recipe_id']
        ingredient = RecipesIngredient.objects.filter(id=ingredient_id, recipe_id=recipe_id).first()
        if not ingredient:
            raise Http404("Ingredient not found")
        return ingredient

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = get_object_or_404(Recipe, pk=self.kwargs['recipe_id'])
        return context

    def get_success_url(self):
        recipe_id = self.kwargs['recipe_id']
        return reverse_lazy('manage-ingredients', kwargs={'recipe_id': recipe_id})

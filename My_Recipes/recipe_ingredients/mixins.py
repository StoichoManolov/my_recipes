from django.shortcuts import redirect, get_object_or_404

from My_Recipes.recipes.models import Recipe


class CheckForRestrictionIngredients:

    def dispatch(self, request, *args, **kwargs):
        # Ensure that the recipe exists
        recipe_id = kwargs.get('recipe_id')

        # Check if the recipe belongs to the current user or if the user is an admin
        recipe = get_object_or_404(Recipe, id=recipe_id)

        if request.user != recipe.created_by and not request.user.is_superuser and not request.user.is_staff:
            return redirect('home')

        # If the user has the right permissions, allow the view to continue
        return super().dispatch(request, *args, **kwargs)
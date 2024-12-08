from django.shortcuts import redirect


class CheckForRestrictionRecipes:

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if request.user != self.object.created_by and not request.user.is_superuser and not request.user.is_staff:
            return redirect('recipe-list')

        return super().dispatch(request, *args, **kwargs)

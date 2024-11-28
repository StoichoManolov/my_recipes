from django.shortcuts import redirect


class CheckForRestrictionRecipes:

    def dispatch(self, request, *args, **kwargs):

        data = super().dispatch(request, *args, **kwargs)

        if request.user != self.object.user and not request.user.is_superuser and not request.user.is_staff:
            return redirect('home')

        return data
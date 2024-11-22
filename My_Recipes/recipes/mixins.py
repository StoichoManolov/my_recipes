from django.shortcuts import redirect


class CheckForRestrictionRecipes:

    def dispatch(self, request, *args, **kwargs):

        data = super().dispatch(request, *args, **kwargs)

        if request.user != self.object.created_by and not request.user.is_superuser and not request.user.is_staff:
            return redirect('home')

        return data


class NotApprovedContent:

    def dispatch(self, request, *args, **kwargs):
        data = super().dispatch(request, *args, **kwargs)
        if not self.object.approved and request.user.pk != self.object.owner.pk and \
                not request.user.is_staff and not request.user.is_superuser:
            return redirect('home-page')

        return data

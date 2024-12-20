from django.shortcuts import redirect


class CheckForRestriction:

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs['pk'] and not request.user.is_superuser:
            return redirect('home')

        data = super().dispatch(request, *args, **kwargs)
        return data


class CheckForRegisteredUser:

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')

        data = super().dispatch(request, *args, **kwargs)
        return data
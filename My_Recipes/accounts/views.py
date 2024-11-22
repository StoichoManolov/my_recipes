from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from My_Recipes.accounts.forms import CustomUserCreationForm, AccountsBaseForm
from My_Recipes.accounts.mixins import CheckForRegisteredUser, CheckForRestriction
from My_Recipes.accounts.models import RecipesUser, Profile


class CreateAccountView(CheckForRegisteredUser, CreateView):

    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')


class DetailAccountView(DetailView):

    model = RecipesUser
    template_name = 'accounts/detail-account.html'
    context_object_name = 'user'

    def get_object(self):
        return get_object_or_404(RecipesUser, pk=self.kwargs["pk"])


class EditAccountView(LoginRequiredMixin, CheckForRestriction, UpdateView):
    model = Profile
    form_class = AccountsBaseForm
    template_name = 'accounts/edit-account.html'

    # This redirects to the user detail view after saving
    success_url = reverse_lazy('detail-account')

    def get_object(self, queryset=None):
        # Get the profile of the currently logged-in user
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy('detail-account', kwargs={'pk': self.object.user.pk})


class DeleteAccountView(CheckForRestriction, DeleteView):

    model = RecipesUser
    success_url = reverse_lazy('home')
    template_name = 'accounts/delete-account.html'

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, FormView

from My_Recipes.accounts.forms import CustomUserCreationForm, AccountsBaseForm, EmailChangeForm
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


class EditAccountView(LoginRequiredMixin, CheckForRestriction, UpdateView):

    model = Profile
    form_class = AccountsBaseForm
    template_name = 'accounts/edit-account.html'

    def get_success_url(self):
        return reverse_lazy('detail-account', kwargs={'pk': self.object.user.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_id = self.object.user.pk

        context['user_id'] = user_id

        return context


class DeleteAccountView(LoginRequiredMixin, CheckForRestriction, DeleteView):

    model = RecipesUser
    success_url = reverse_lazy('home')
    template_name = 'accounts/delete-account.html'


class PasswordChange(CheckForRestriction, PasswordChangeView):
    model = RecipesUser

    def get_success_url(self):
        return reverse_lazy('detail-account', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        messages.success(self.request, 'Password changed successfully!')
        return super().form_valid(form)


class EmailChangeView(LoginRequiredMixin, CheckForRestriction, FormView):

    template_name = "registration/email_change_form.html"
    form_class = EmailChangeForm

    def form_valid(self, form):
        new_email = form.cleaned_data['email']

        self.request.user.email = new_email
        self.request.user.save()

        messages.success(self.request, "Your email has been updated successfully!")

        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs['user'] = self.request.user  # Pass the logged-in user to the form

        return kwargs

    def get_success_url(self):
        return reverse_lazy('detail-account', kwargs={'pk': self.request.user.pk})


class CustomLoginView(CheckForRegisteredUser, LoginView):

    template_name = 'registration/login.html'

from django import forms
from django.contrib.auth.forms import UserCreationForm

from My_Recipes.accounts.models import Profile, RecipesUser


class AccountsBaseForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ('user', )


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = RecipesUser
        fields = ('username', 'email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'  # Adding bootstrap class for styling


class EmailChangeForm(forms.Form):
    email = forms.EmailField(label="New Email", max_length=254)
    confirm_email = forms.EmailField(label="Confirm New Email", max_length=254)
    password = forms.CharField(widget=forms.PasswordInput, label="Current Password")

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")

        # Check if the two email addresses match
        if email != confirm_email:
            self.add_error('confirm_email', "The email addresses do not match.")

        # Check if the new email already exists
        elif RecipesUser.objects.filter(email=email).exists():
            # Add the error to the 'email' field explicitly
            self.add_error('email', "This email address is already in use.")

        return cleaned_data

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not self.user.check_password(password):
            raise forms.ValidationError("The current password is incorrect.")
        return password

    def __init__(self, *args, **kwargs):
        # Passing the user to the form to validate the password and check if email exists
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
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


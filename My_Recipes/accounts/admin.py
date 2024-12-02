from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


# Register your models here.
UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'created_at')
    fields = (
        'username',
        'email',
        'password',
        'is_staff',
        'is_superuser',
        'groups')
    ordering = ('username', 'email')
    list_filter = ['username', 'is_superuser', 'is_staff', 'created_at']
    search_fields = ('username', 'email', 'is_superuser', 'is_staff')

    def save_model(self, request, obj, form, change):
        """Ensure passwords are hashed when saved."""
        if 'password' in form.changed_data:
            obj.set_password(form.cleaned_data['password'])
        obj.save()
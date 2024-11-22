from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.
UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    fields = (
        'email',
        'is_staff',
        'is_superuser',
        'groups')
    ordering = ('username', 'email')
    list_filter = ['username', 'is_superuser', 'is_staff']
    search_fields = ('username', 'email' ,'is_superuser', 'is_staff')
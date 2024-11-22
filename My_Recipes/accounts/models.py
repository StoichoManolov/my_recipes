from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from My_Recipes.accounts.managers import RecipeManager
from My_Recipes.accounts.validators import is_it_alpha


# Create your models here.


class RecipesUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        unique=True,
        max_length=20,
        validators=[MinLengthValidator(3)],
    )

    email = models.EmailField(
        unique=True,
        max_length=30,
    )

    created_at = models.DateField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = RecipeManager()

    USERNAME_FIELD = 'username'  # Default login field is username

    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username


class Profile(models.Model):

    user = models.OneToOneField(
        RecipesUser,
        on_delete=models.CASCADE,
        related_name='profile',
    )

    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        validators=[MinLengthValidator(2),
                    is_it_alpha],
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        validators=[MinLengthValidator(2),
                    is_it_alpha],
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    profile_picture = models.ImageField(
        blank=True,
        null=True,
        upload_to='photos/profile_pictures',
    )




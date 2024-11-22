from django.core import exceptions


def is_it_alpha(value):
    if not value.isalpha():
        raise exceptions.ValidationError('Name must be only alphabet symbol!')
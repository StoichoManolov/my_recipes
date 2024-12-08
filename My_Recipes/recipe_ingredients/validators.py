from django.core import exceptions


def is_it_digit(value):
    if not value.isdigit():
        raise exceptions.ValidationError('Quantity should be a number!')

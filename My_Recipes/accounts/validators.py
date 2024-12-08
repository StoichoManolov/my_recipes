from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class EmptySpacesOrAlphaValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Ensure this value contains only letters."
        else:
            self.__message = value

    def __call__(self, value):
        if not all(word.isalpha() for word in value.split()):
            raise ValidationError(self.message)
        elif ' ' in value:
            raise(ValidationError(self.message))




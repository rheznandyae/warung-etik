from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    error_messages = {
        'password_mismatch': "Password missmatch",
    }
    class Meta:
        model = User
        fields = ['username', 'email' ,'password1', 'password2']
        error_messages = {
            'username': {
                'unique': 'Username is already taken',
            },
        }

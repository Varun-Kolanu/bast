from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model



class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    # class Meta(AuthenticationForm.Meta):
    #     model = get_user_model()
    #     fields = ('username', 'password')
    pass
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm
from .models import CustomUser


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    
    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone", "country", "password1", "password2")
        
        
class EditUserForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone", "country", "avatar", "background", "is_private")
        help_texts = {
            "username": None
        }
        
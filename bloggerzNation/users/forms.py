from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import ProfileModel


# Form for signing up
class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User    # This form is built on User model
        fields = ['username', 'email', 'password1', 'password2']    # Fileds to be displayed in form

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # Removing helping text in the form
        for field in ['username', 'email', 'password1', 'password2']:
            self.fields[field].help_text = None


# Form for updating information of User
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User    # This form is built on User model
        fields = ['username', 'email']
    
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        # Removing helping text in the form
        self.fields['username'].help_text = None
        self.fields['email'].help_text = None


# Form to update profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['image']


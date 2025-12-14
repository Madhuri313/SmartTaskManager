from django import forms
from django.contrib.auth.models import User
class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm password')
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','password','password2')
        help_texts = {
            'username': None,  # Removes the default message
        }
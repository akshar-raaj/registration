from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    """
    Default registration form to be used with registration
    Shows three fields on page
    username: A character field. Is required
    password: Required
    Confirm password: Required
    """
    username = forms.CharField(max_length=30, required=True)
    password1 = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', max_length=30, widget=forms.PasswordInput)
    
    def clean_username(self):
        try:
            User.objects.get(username=self.cleaned_data['username'])
            raise forms.ValidationError("This username is taken")
        except User.DoesNotExist:
            return self.cleaned_data['username']

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if not self.cleaned_data['password1'] == self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords must match")
        return self.cleaned_data

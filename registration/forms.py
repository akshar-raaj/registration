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
    email = forms.EmailField()
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
            raise forms.ValidationError("This username is taken")
        except User.DoesNotExist:
            return username

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
            raise forms.ValidationError("This email is taken")
        except User.DoesNotExist:
            return email

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if not self.cleaned_data['password1'] == self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords must match")
        return self.cleaned_data

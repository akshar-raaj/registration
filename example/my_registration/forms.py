from django import forms

from registration.forms import RegistrationForm

class MyRegistrationForm(RegistrationForm):
    """
    Default registration form only allows username, email
    and password.
    We want a first_name, last_name as well as Organization name
    We will save organization name as part of Profile
    """
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    organization_name = forms.CharField(max_length=30)

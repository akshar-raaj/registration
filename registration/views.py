from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from .forms import RegistrationForm


def register(request, form_class=RegistrationForm,
             template_name='registration/register.html',
             redirect_url='registration_register_done', **kwargs):
    form = form_class()
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            process_registration_form(request, form)
            return HttpResponseRedirect(reverse(redirect_url))
    data = {'registration_form': form}
    data.update(kwargs)
    return render(request, template_name, data)

def process_registration_form(request, form):
    """
    Expects following arguments:
    request: HttpRequest instance
    Valid POSTed form
    Creates a User instance with POSTed form
    """
    if 'username' not in form.cleaned_data:
        form.cleaned_data['username'] = ''
    user_data = {}
    user_fields = [f.name for f in User._meta.fields]
    for field, value in form.cleaned_data.items():
        if field in user_fields:
            user_data[field] = value
    user = User.objects.create_user(**user_data)
    return user

def register_done(request, template_name='registration/register_done.html',
                  **kwargs):
    data = {}
    data.update(kwargs)
    return render(request, template_name, data)

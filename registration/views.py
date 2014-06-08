from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView

from .forms import RegistrationForm
from .signals import registered


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('registration_register_done')

    def form_valid(self, form):
        # A valid form is POSTed
        self.process_registration_form(self.request, form)
        registered.send(sender=User, request=self.request, form=form)
        return super(RegisterView, self).form_valid(form)

    def process_registration_form(self, request, form):
        """
        Expects following arguments:
        request: HttpRequest instance
        Valid POSTed form
        Creates a User instance with POSTed form
        """
        user_data = {}
        user_fields = [f.name for f in User._meta.fields]
        for field, value in form.cleaned_data.items():
            if field in user_fields:
                user_data[field] = value
        user = User.objects.create_user(**user_data)
        return user

register = RegisterView.as_view()


def register_done(request, template_name='registration/register_done.html',
                  **kwargs):
    data = {}
    data.update(kwargs)
    return render(request, template_name, data)

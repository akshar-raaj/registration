from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView

from .forms import RegistrationForm
from .signals import registered
from .conf import REGISTRATION_MAKE_USER_INACTIVE
from .models import ActivationKey


class RegisterView(FormView):
    """
    This is the default view with the most basic workflow.
    This uses a Form, which will have the same field names as 
    field name on model User.
    The form can have extra fields too, i.e non-User fields.
    A User is created with the POSTed data and this view
    optionally provides setting user as active or inactive.
    We will write a separate view which can handle email verification.
    """
    template_name = 'registration/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('registration_register_done')

    def form_valid(self, form):
        # A valid form is POSTed
        user = self.process_registration_form(form)
        registered.send(sender=User, request=self.request, form=form, user=user)
        return super(RegisterView, self).form_valid(form)

    def process_registration_form(self, form):
        """
        Expects following arguments:
        Valid POSTed form
        Creates a User instance with POSTed form
        """
        user = self.create_user(form)
        self.change_user_is_active(user)
        return user

    def create_user(self, form):
        """
        Creates a User instance with POSTed form
        """
        user_data = {}
        user_fields = [f.name for f in User._meta.fields]
        for field, value in form.cleaned_data.items():
            if field in user_fields:
                user_data[field] = value
        return User.objects.create_user(**user_data)

    def change_user_is_active(self, user):
        if REGISTRATION_MAKE_USER_INACTIVE:
            user.is_active = False
            user.save()

class RegisterAndSendEmailVerificationView(RegisterView):
    """
    This view would use a registration form.
    The form **must** have an email field to which
    the verification link can be sent.
    """

    def process_registration_form(self, form):
        user = super(RegisterAndSendEmailVerificationView, self).process_registration_form(form)
        # Send an activation link to this user
        ActivationKey.objects.send_activation_email(user)
        # We allow customizing the mail subject
        # and mail body
        return user

    def change_user_is_active(self, user):
        """
        If an email verification link is being sent,
        you must be wanting to set the user inactive initially.
        If you don't want this behaviour, subclass this view
        and override this method.
        """
        user.is_active = False
        user.save()


def register_done(request, template_name='registration/register_done.html',
                  **kwargs):
    data = {}
    data.update(kwargs)
    return render(request, template_name, data)

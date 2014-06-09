from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.template.loader import render_to_string
from django.contrib.sites.models import Site

from .conf import REGISTRATION_FROM_EMAIL

class ActivationKeyManager(models.Manager):

    registration_mail_subject = 'registration/registration_mail_subject.txt'
    registration_mail_body = 'registration/registration_mail_body.txt'

    def send_activation_email(self, user):
        self.user = user
        key = get_random_string()
        activation_key = self.create(key=key, user=user)
        site = Site.objects.get_current()
        subject = render_to_string(self.registration_mail_subject, {'site': site, 'user': user})
        body = render_to_string(self.registration_mail_body, {'site': site, 'user':user, 'activation_key': activation_key})
        self.send_email(subject, body)

    def send_email(self, subject, message):
        """
        TODO: Will allow queuing here.
        """
        send_mail(subject, message, REGISTRATION_FROM_EMAIL, [self.user.email])


class ActivationKey(models.Model):
    """
    When a User registers, an email with verification
    link is sent to him.
    Verification link contains an activation key.
    He will click this verification link and then his
    account will be marked as active. But to achieve it,
    we need an association between User and activation key.
    This model associates User with the activation key
    """
    objects = ActivationKeyManager()

    key = models.CharField(max_length=12, unique=True)
    """
    Activation link will only be valid for a fixed period.
    So, user should be able to request another
    verification link.
    So, it's a FK and not a OneToOneField.
    """
    user = models.ForeignKey(User)

    is_active = models.BooleanField(default=False)

    def mark_active(self):
        self.is_active = True
        self.save()

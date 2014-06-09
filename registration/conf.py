from django.conf import settings

# Set this to True if you want the registered users to be inactive initially
REGISTRATION_MAKE_USER_INACTIVE = getattr(settings, 'REGISTRATION_MAKE_USER_INACTIVE', False)
# This app allows sending verification link to registered user
# Set this to the address from which the links should be sent
REGISTRATION_FROM_EMAIL = getattr(settings, 'REGISTRATION_FROM_EMAIL', settings.DEFAULT_FROM_EMAIL)

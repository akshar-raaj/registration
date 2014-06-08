from django.conf import settings

# Set this to True if you want the registered users to be inactive initially
REGISTRATION_MAKE_USER_INACTIVE = getattr(settings, 'REGISTRATION_MAKE_USER_INACTIVE', False)

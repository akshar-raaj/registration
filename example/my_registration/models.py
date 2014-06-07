from registration.signals import registered


def registration_callback(sender, **kwargs):
    pass

registered.connect(registration_callback)

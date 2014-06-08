import django.dispatch

registered = django.dispatch.Signal(providing_args=["request", "form", "user"])

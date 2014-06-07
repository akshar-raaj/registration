from django.conf.urls import patterns, url

from .forms import MyRegistrationForm

urlpatterns = patterns('',
        url(r'^register/$', 'registration.views.register', kwargs={'form_class': MyRegistrationForm}, name='registration_register'),
)

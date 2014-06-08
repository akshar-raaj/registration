from django.conf.urls import patterns, url

from registration.views import RegisterView

from .forms import MyRegistrationForm

urlpatterns = patterns('',
    url(r'^register/$', RegisterView.as_view(form_class=MyRegistrationForm), name='registration_register'),
)

from django.conf.urls import patterns, url

from .views import RegisterView, register_done


urlpatterns = patterns('',
    url(r'^register/$', RegisterView.as_view(), name='registration_register'),
    url(r'^register/done/$', register_done, name='registration_register_done'),
)

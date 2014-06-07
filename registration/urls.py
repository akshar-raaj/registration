from django.conf.urls import patterns, url

from .views import register, register_done


urlpatterns = patterns('',
    url(r'^register/$', register, name='registration_register'),
    url(r'^register/done/$', register_done, name='registration_register_done'),
)

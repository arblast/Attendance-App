from django.conf.urls import url

from . import views

app_name = 'attendance'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<attendee_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<attendee_id>[0-9]+)/edit/$', views.edit, name='edit'),
]

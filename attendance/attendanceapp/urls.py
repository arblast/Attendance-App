from django.conf.urls import url
from attendanceapp import views
from django.views.generic import TemplateView
from attendanceapp.views import Attendee

urlpatterns = [
    url(r'^hello/', views.hello, name='hello'),
    url(r'^connection/', TemplateView.as_view(template_name = 'login.html')),
    url(r'^login/', views.login, name = 'login'),
    url(r'^attendee/new', Attendee.as_view(), name = 'attendee'),
]

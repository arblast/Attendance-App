from django.conf.urls import url
from attendanceapp import views
from django.views.generic import TemplateView
from attendanceapp.views import AttendeeView
from attendanceapp.views import DateView

urlpatterns = [
    url(r'^hello/', views.hello, name='hello'),
    url(r'^connection/', TemplateView.as_view(template_name = 'login.html')),
    url(r'^login/', views.login, name = 'login'),
    url(r'^attendee/', AttendeeView.as_view(), name = 'attendee'),
    url(r'^date/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})', DateView.as_view(), name = 'dateget'),
]

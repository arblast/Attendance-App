from django.conf.urls import url
from attendanceapp import views

urlpatterns = [
    url(r'^hello/', views.hello, name='hello'),
]

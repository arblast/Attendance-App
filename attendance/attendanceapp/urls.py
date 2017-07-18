from django.conf.urls import url
from attendanceapp import views
from django.views.generic import TemplateView
from attendanceapp.views import AttendeeCreate

urlpatterns = [
    url(r'^hello/', views.hello, name='hello'),
    url(r'article/(\d+)/', views.viewArticle, name='article'),
    url(r'articles/(?P<month>\d{2})/(?P<year>\d{4})', views.viewArticles, name='articles'),
    url(r'^connection/', TemplateView.as_view(template_name = 'login.html')),
    url(r'^login/', views.login, name = 'login'),
    url(r'^attendee/new', AttendeeCreate.as_view(), name = 'new'),
]

from django.conf.urls import url
from attendanceapp import views

urlpatterns = [
    url(r'^hello/', views.hello, name='hello'),
    url(r'article/(\d+)/', views.viewArticle, name='article'),
    url(r'articles/(?P<month>\d{2})/(?P<year>\d{4})', views.viewArticles, name='articles'),
]

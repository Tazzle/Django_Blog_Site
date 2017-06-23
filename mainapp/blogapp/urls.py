#blogapp/urls.py

from django.conf.urls import url
from blogapp import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^blogpost/$', views.BlogPageView.as_view()),
    url(r'^createblog/$', views.CreateBlogPageView.as_view()),
]
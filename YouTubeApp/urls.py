from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^get_popular_themes/', views.popular_themes, name='popular_themes'),
)

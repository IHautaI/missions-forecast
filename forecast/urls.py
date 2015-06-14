from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^specialist/(?P<specialist_id>[0-9]+)/$', views.specialist, name='specialist'),
    url(r'^country/(?P<country_name>(?:\w+\s?)+)/$', views.country, name='country'),
    url(r'^code/(?P<code>[\w\.-]+)/$', views.NAICS, name='NAICS'),
]

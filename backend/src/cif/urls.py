from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lookup/(?P<cif>[a-zA-Z0-9]{9})/$', views.lookup, name='lookup'),
]

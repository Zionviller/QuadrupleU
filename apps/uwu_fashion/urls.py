from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^upload$', views.upload),
    url(r'^profile$', views.profile),
    url(r'^process_upload$', views.process_upload),
]

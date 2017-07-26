from django.conf.urls import url

from . import views
app_name = 'gnng'

urlpatterns = [
    url(r'^notifviewer/$', views.notifviewer, name='notifviewer'),
    url(r'^docchatviewer/$', views.docchatviewer, name='docchatviewer'),
    ]

from django.conf.urls import url

from . import views

app_name = 'csvimport'
urlpatterns = [
    # /csvimport
    url(r'^$', views.index, name='csvindex'),
]
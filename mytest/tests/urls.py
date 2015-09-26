from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /tests/
    url(r'^$', views.index, name='index'),
    # ex: /tests/5/
    url(r'^(?P<key_id>[0-9]+)/$', views.detail, name='detail'),
]

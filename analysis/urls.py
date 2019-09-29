from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^1$', views.analysis1, name="analysis1"),
    url(r'^search1$', views.search1, name="search1"),
    url(r'^2$', views.analysis2, name="analysis2"),
]
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^1$', views.analysis1, name="analysis1"),
    url(r'^search1$', views.search1, name="search1"),
    url(r'^2$', views.analysis2, name="analysis2"),
    url(r'^search2$', views.search2, name="search2"),
    url(r'^3$', views.analysis3, name="analysis3"),
    url(r'^search3$', views.search3, name="search3"),
    url(r'^4$', views.analysis4, name="analysis4"),
    url(r'^search4$', views.search4, name="search4"),
    url(r'^5$', views.analysis5, name="analysis5"),
    url(r'^search5$', views.search5, name="search5"),
]
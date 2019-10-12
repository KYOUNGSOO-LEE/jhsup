from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^1$', views.analysis1, name="analysis1"),
    url(r'^search1$', views.search1, name="search1"),
    url(r'^2$', views.analysis2, name="analysis2"),
    url(r'^search2$', views.search2, name="search2"),
    url(r'^3$', views.analysis3, name="analysis3"),
    url(r'^search3$', views.search3, name="search3"),
    url(r'^ajax/load_univ_name$', views.load_univ_name, name="ajax_load_univ_name"),
    url(r'^ajax/load_univ_major$', views.load_univ_major, name="ajax_load_univ_major"),
    url(r'^ajax/load_admission1$', views.load_admission1, name="ajax_load_admission1"),
    url(r'^ajax/load_admission2$', views.load_admission2, name="ajax_load_admission2"),
]
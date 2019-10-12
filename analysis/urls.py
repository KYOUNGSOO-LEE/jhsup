from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^grade$', views.grade, name="grade"),
    url(r'^grade_search$', views.grade_search, name="grade_search"),
    url(r'^major$', views.major, name="major"),
    url(r'^major_search$', views.major_search, name="major_search"),
    url(r'^advanced$', views.advanced, name="advanced"),
    url(r'^advanced_search$', views.advanced_search, name="advanced_search"),
    url(r'^university$', views.university, name="university"),
    url(r'^university_search$', views.university_search, name="university_search"),
    url(r'^ajax/load_univ_name$', views.load_univ_name, name="ajax_load_univ_name"),
    url(r'^ajax/load_univ_major$', views.load_univ_major, name="ajax_load_univ_major"),
    url(r'^ajax/load_admission1$', views.load_admission1, name="ajax_load_admission1"),
]
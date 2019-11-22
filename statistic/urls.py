from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^app-region$', views.app_region, name="app_region"),
    url(r'^app-region-search$', views.app_region_search, name="app_region_search"),

    url(r'^app-grade$', views.app_grade, name="app_grade"),
    url(r'^app-grade-search$', views.app_grade_search, name="app_grade_search"),
]
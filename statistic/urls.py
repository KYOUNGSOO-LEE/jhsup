from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^student-region$', views.entrance_year, name="static_entrance_year"),
    url(r'^student-region-result$', views.entrance_year_result, name="static_entrance_year_result"),

    url(r'^admission1$', views.admission1, name="static_admission1"),
    url(r'^admission1-result$', views.admission1_result, name="static_admission1_result"),

    url(r'^univ-region$', views.univ_region, name="static_univ_region"),
    url(r'^univ-region-result$', views.univ_region_result, name="static_univ_region_result"),

    url(r'^major-group$', views.major_group, name="major_group"),
    url(r'^major-group-result$', views.major_group_result, name="major_group_result"),
]
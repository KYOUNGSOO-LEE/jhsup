from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^student-region$', views.student_region, name="static_student_region"),
    url(r'^student-region-result$', views.student_region_result, name="static_student_region_result"),

    url(r'^admission1$', views.admission1, name="static_admission1"),
    url(r'^admission1-result$', views.admission1_result, name="static_admission1_result"),

    url(r'^univ-region$', views.univ_region, name="static_univ_region"),
    url(r'^univ-region-result$', views.univ_region_result, name="static_univ_region_result"),
]
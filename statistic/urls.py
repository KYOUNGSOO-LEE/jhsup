from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^student-region$', views.student_region, name="static_student_region"),
    url(r'^student-region-result$', views.student_region_result, name="static_student_region_result"),

    url(r'^grade$', views.grade, name="static_grade"),
    url(r'^grade-result$', views.grade_result, name="static_grade_result"),

    url(r'^admission1$', views.admission1, name="static_admission1"),
    url(r'^admission1-result$', views.admission1_result, name="static_admission1_result"),
]
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^static-student-region$', views.static_student_region, name="static_student_region"),
    url(r'^static-student-region-result$', views.static_student_region_result, name="static_student_region_result"),

    url(r'^static_grade$', views.static_grade, name="static_grade"),
    url(r'^static-grade-result$', views.static_grade_result, name="static_grade_result"),
]
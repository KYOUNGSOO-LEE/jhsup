from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^student-region$', views.static_student_region, name="static_student_region"),
    url(r'^student-region-result$', views.static_student_region_result, name="static_student_region_result"),

    url(r'^grade$', views.static_grade, name="static_grade"),
    url(r'^grade-result$', views.static_grade_result, name="static_grade_result"),
]
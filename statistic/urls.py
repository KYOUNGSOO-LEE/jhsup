from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^student-region$', views.student_region, name="static_student_region"),
    url(r'^student-region-result$', views.student_region_result, name="static_student_region_result"),

    url(r'^grade$', views.grade, name="static_grade"),
    url(r'^grade-result$', views.grade_result, name="static_grade_result"),

    url(r'^admission$', views.admission, name="static_admission"),
    url(r'^admission-result$', views.admission_result, name="static_admission_result"),
]
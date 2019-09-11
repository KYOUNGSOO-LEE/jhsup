from django.db import models

# Create your models here.
# gubun1 : 일반대/특수대/산업대, gubun2 : 지역(서울 등)
# addmission1 : 교과/논술/실기/종합
# addmission2 : 세부유형
class ibsi(models.Model):
    ibsi_year = models.IntegerField()
    gubun1 = models.CharField(max_length = 3)
    resion = models.CharField(max_length = 2)
    gubun2 = models.CharField(max_length = 3)
    univ_name = models.CharField(max_length = 10)
    major = models.CharField(max_length = 10)
    admission1 = models.CharField(max_length = 2)
    admission2 = models.CharField(max_length = 20)
    all_subject_100 = models.DecimalField(decimal_places = 3, max_digits = 4)
    ko_en_math_soc_100 = models.DecimalField(decimal_places = 3, max_digits = 4)
    ko_en_math_sci_100 = models.DecimalField(decimal_places = 3, max_digits = 4)
    change_grade = models.DecimalField(decimal_places = 3, max_digits = 4)
    first_step = models.CharField(max_length = 5, blank = True)
    final_step = models.CharField(max_length = 5)
    fail_reason = models.CharField(max_length = 10, blank = True)
    num_students = models.IntegerField(blank = True)

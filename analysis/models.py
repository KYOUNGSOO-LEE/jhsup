from django.db import models


class Student(models.Model):
    entrance_year = models.IntegerField()  # 입시학년도
    student_region = models.CharField(max_length=3)  # 수합지역
    univ_group = models.CharField(max_length=3)  # 일반대/특수대/산업대
    univ_region = models.CharField(max_length=2)  # 대학소재
    major_group = models.CharField(max_length=3)  # 계열
    univ_name = models.CharField(max_length=10)  # 대학명
    univ_major = models.CharField(max_length=10)  # 모집단위
    admission1 = models.CharField(max_length=2)  # 전형유형(교과/논술/실시/종합)
    admission2 = models.CharField(max_length=20)  # 세부유형(일반전형/농어촌학생 등)
    admission3 = models.CharField(max_length=10)  # 선발유형(일괄합산/1단계 등)
    grade = models.DecimalField(decimal_places=3, max_digits=4, null=True)  # 등급(대학별 환산등급)
    univ_score = models.DecimalField(decimal_places=3, max_digits=10, null=True)  # 대학별 환산점수
    korean = models.DecimalField(decimal_places=3, max_digits=4)  # 국어
    english = models.DecimalField(decimal_places=3, max_digits=4)  # 영어
    mathematics = models.DecimalField(decimal_places=3, max_digits=4)  # 수학
    society = models.DecimalField(decimal_places=3, max_digits=4)  # 사회
    science = models.DecimalField(decimal_places=3, max_digits=4)  # 과학
    all_subject_100 = models.DecimalField(decimal_places=3, max_digits=4)  # 전교과100
    all_subject_244 = models.DecimalField(decimal_places=3, max_digits=4)  # 전교과244
    all_subject_433 = models.DecimalField(decimal_places=3, max_digits=4)  # 전교과433
    all_subject_235 = models.DecimalField(decimal_places=3, max_digits=4)  # 전교과235
    ko_en_math_soc_sci_100 = models.DecimalField(decimal_places=3, max_digits=4)  # 국영수사과100
    ko_en_math_soc_sci_244 = models.DecimalField(decimal_places=3, max_digits=4)  # 국영수사과244
    ko_en_math_soc_sci_334 = models.DecimalField(decimal_places=3, max_digits=4)  # 국영수사과334
    ko_en_math_soc_sci_433 = models.DecimalField(decimal_places=3, max_digits=4)  # 국영수사과433
    ko_en_math_100 = models.DecimalField(decimal_places=3, max_digits=4)  # 국영수100
    ko_en_math_soc_100 = models.DecimalField(decimal_places=3, max_digits=4)  # 국영수사100
    ko_en_math_soc_244 = models.DecimalField(decimal_places=3, max_digits=4)  # 국영수사244
    ko_en_math_soc_334 = models.DecimalField(decimal_places=3, max_digits=4)  # 국영수사334
    ko_en_math_soc_433 = models.DecimalField(decimal_places=3, max_digits=4)  # 국영수사433
    ko_en_math_soc_370 = models.DecimalField(decimal_places=3, max_digits=4)  # 국영수사3/[70]
    ko_en_soc_100 = models.DecimalField(decimal_places=3, max_digits=4)  # 국영사100
    ko_en_soc_244 = models.DecimalField(decimal_places=3, max_digits=4)  # 국영사244
    ko_en_math_sci_100 = models.DecimalField(decimal_places=3, max_digits=4)  # 국영수과100
    ko_en_math_sci_244 = models.DecimalField(decimal_places=3, max_digits=4)  # 국영수과244
    ko_en_math_sci_334 = models.DecimalField(decimal_places=3, max_digits=4)  # 국영수과334
    ko_en_math_sci_433 = models.DecimalField(decimal_places=3, max_digits=4)  # 국영수과433
    ko_en_math_sci_370 = models.DecimalField(decimal_places=3, max_digits=4)  # 국영수과3/[70]
    en_math_sci_100 = models.DecimalField(decimal_places=3, max_digits=4)  # 수영과100
    en_math_sci_244 = models.DecimalField(decimal_places=3, max_digits=4)  # 수영과244
    first_step = models.CharField(max_length=5, null=True)  # 1단계 합격/불합격
    final_step = models.CharField(max_length=5)  # 최종 합격/불합격
    fail_reason = models.CharField(max_length=10, null=True)  # 불합격 사유
    candidate_rank = models.IntegerField(null=True)  # 최초 후보순위
    num_students = models.IntegerField(null=True)  # 모집인원


    def __str__(self):
        return f'{self.univ_name} {self.univ_major}'

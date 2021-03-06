from django.db import models


class UnivGroup(models.Model):
    univ_group = models.CharField(max_length=3)  # 일반대/특수대/산업대

    def __str__(self):
        return self.univ_group


class UnivRegion(models.Model):
    univ_region = models.CharField(max_length=2)  # 대학소재

    def __str__(self):
        return self.univ_region


class MajorGroup(models.Model):
    major_group = models.CharField(max_length=3)  # 계열

    def __str__(self):
        return self.major_group


class UnivName(models.Model):
    univ_name = models.CharField(max_length=10)  # 대학명
    univ_group = models.ForeignKey('UnivGroup', on_delete=models.CASCADE)  # 일반대/특수대/산업대
    univ_region = models.ForeignKey('UnivRegion', on_delete=models.CASCADE)  # 대학소재

    def __str__(self):
        return self.univ_name


class UnivMajor(models.Model):
    univ_major = models.CharField(max_length=10)  # 모집단위
    major_group = models.ForeignKey('MajorGroup', on_delete=models.CASCADE)  # 계열
    univ_name = models.ForeignKey('UnivName', on_delete=models.CASCADE)  # 대학명

    def __str__(self):
        return self.univ_major


class Admission1(models.Model):
    admission1 = models.CharField(max_length=2)  # 전형유형(교과/논술/실시/종합)
    univ_name = models.ForeignKey('UnivName', on_delete=models.CASCADE)  # 대학명
    univ_major = models.ForeignKey('UnivMajor', on_delete=models.CASCADE)  # 모집단위

    def __str__(self):
        return self.admission1


class Admission2(models.Model):
    admission2 = models.CharField(max_length=10)  # 세부유형(일반전형/농어촌학생 등)
    univ_name = models.ForeignKey('UnivName', on_delete=models.CASCADE)  # 대학명
    univ_major = models.ForeignKey('UnivMajor', on_delete=models.CASCADE)  # 모집단위
    admission1 = models.ForeignKey('Admission1', on_delete=models.CASCADE)  # 전형유형(교과/논술/실시/종합)

    def __str__(self):
        return self.admission2


class Admission3(models.Model):
    admission3 = models.CharField(max_length=10)  # 선발유형(일괄합산/1단계 등)
    univ_name = models.ForeignKey('UnivName', on_delete=models.CASCADE)  # 대학명
    univ_major = models.ForeignKey('UnivMajor', on_delete=models.CASCADE)  # 모집단위
    admission1 = models.ForeignKey('Admission1', on_delete=models.CASCADE)  # 전형유형(교과/논술/실시/종합)
    admission2 = models.ForeignKey('Admission2', on_delete=models.CASCADE)  # 세부유형(일반전형/농어촌학생 등)

    def __str__(self):
        return self.admission3


class Personnel(models.Model):
    personnel = models.IntegerField(null=True)  # 모집인원
    univ_name = models.ForeignKey('UnivName', on_delete=models.CASCADE)  # 대학명
    univ_major = models.ForeignKey('UnivMajor', on_delete=models.CASCADE)  # 모집단위
    admission1 = models.ForeignKey('Admission1', on_delete=models.CASCADE)  # 전형유형(교과/논술/실시/종합)
    admission2 = models.ForeignKey('Admission2', on_delete=models.CASCADE)  # 세부유형(일반전형/농어촌학생 등)

    def __str__(self):
        return self.personnel


class Student(models.Model):
    entrance_year = models.IntegerField()  # 입시학년도
    student_region = models.CharField(max_length=3)  # 수합지역
    univ_group = models.ForeignKey('UnivGroup', on_delete=models.CASCADE)  # 일반대/특수대/산업대
    univ_region = models.ForeignKey('UnivRegion', on_delete=models.CASCADE)  # 대학소재
    major_group = models.ForeignKey('MajorGroup', on_delete=models.CASCADE)  # 계열
    univ_name = models.ForeignKey('UnivName', on_delete=models.CASCADE)  # 대학명
    univ_major = models.ForeignKey('UnivMajor', on_delete=models.CASCADE)  # 모집단위
    admission1 = models.ForeignKey('Admission1', on_delete=models.CASCADE)  # 전형유형(교과/논술/실시/종합)
    admission2 = models.ForeignKey('Admission2', on_delete=models.CASCADE)  # 세부유형(일반전형/농어촌학생 등)
    admission3 = models.ForeignKey('Admission3', on_delete=models.CASCADE)  # 선발유형(일괄합산/1단계 등)
    grade = models.DecimalField(decimal_places=3, max_digits=4)  # 등급(대학별 환산등급)
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
    personnel = models.ForeignKey('Personnel', on_delete=models.CASCADE)  # 모집인원


    def __str__(self):
        return f'{self.univ_name} {self.univ_major}'
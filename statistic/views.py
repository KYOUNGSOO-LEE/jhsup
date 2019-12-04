from django.shortcuts import render
from analysis.models import *
from django.db.models import Count, Avg
from django.db.models.functions import Floor
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def student_region(request):
    template = "statistic/student_region.html"

    # 지역별 사례수
    entrance_year_qs = Student.objects.values('entrance_year').order_by('entrance_year').distinct()

    context = {
        'entrance_year_item': entrance_year_qs,
    }
    return render(request, template, context)


@login_required(login_url="login")
def student_region_result(request):
    template = "statistic/student_region_result.html"

    # 지역별 사례수
    entrance_year_qs = Student.objects.values('entrance_year').order_by('entrance_year').distinct()
    entrance_year_query = request.GET.get('entrance_year')
    student_region_query = request.GET.get('student_region')

    student_region_freq_qs = Student.objects\
        .filter(entrance_year=entrance_year_query)\
        .values_list('student_region')\
        .annotate(student_region_count=Count('student_region'))\
        .order_by('-student_region_count')
    student_region_list = []
    student_region_freq_list = []

    for student_region in student_region_freq_qs:
        student_region_list.append(student_region[0])
        student_region_freq_list.append(student_region[1])

    # 지역별 지원대학 현황
    univ_name_list = []
    univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    if student_region_query == '충청도':
        univ_freq_qs = Student.objects\
                           .filter(entrance_year=entrance_year_query)\
                           .values_list('univ_name')\
                           .annotate(univ_count=Count('univ_name'))\
                           .order_by('-univ_count')[:25]
    else:
        univ_freq_qs = Student.objects\
                           .filter(entrance_year=entrance_year_query) \
                           .filter(student_region=student_region_query) \
                           .values_list('univ_name') \
                           .annotate(univ_count=Count('univ_name')) \
                           .order_by('-univ_count')[:25]

    for univ in univ_freq_qs:
        univ_name = univ_name_qs.get(pk=univ[0])
        univ_name_list.append(univ_name.univ_name)
        univ_freq_list.append(univ[1])

    # 지역별 지원대학 합격/불합격 인원
    univ_pass_freq_list = []
    univ_supplement_freq_list = []
    univ_fail_freq_list = []

    if student_region_query == '충청도':
        for univ in univ_name_list:
            univ_name = univ_name_qs.get(univ_name=univ)
            univ_pass_freq_count = Student.objects\
                .filter(entrance_year=entrance_year_query)\
                .filter(univ_name=univ_name.id) \
                .filter(final_step='합격') \
                .count()
            univ_supplement_freq_count = Student.objects\
                .filter(entrance_year=entrance_year_query) \
                .filter(univ_name=univ_name.id) \
                .filter(final_step='충원합격') \
                .count()
            univ_fail_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(univ_name=univ_name.id) \
                .filter(final_step='불합격') \
                .count()
            univ_pass_freq_list.append(univ_pass_freq_count)
            univ_supplement_freq_list.append(univ_supplement_freq_count)
            univ_fail_freq_list.append(univ_fail_freq_count)

    else:
        for univ in univ_name_list:
            univ_name = univ_name_qs.get(univ_name=univ)
            univ_pass_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(student_region=student_region_query)\
                .filter(univ_name=univ_name.id) \
                .filter(final_step='합격') \
                .count()
            univ_supplement_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(student_region=student_region_query) \
                .filter(univ_name=univ_name.id) \
                .filter(final_step='충원합격') \
                .count()
            univ_fail_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(student_region=student_region_query)\
                .filter(univ_name=univ_name.id) \
                .filter(final_step='불합격') \
                .count()
            univ_pass_freq_list.append(univ_pass_freq_count)
            univ_supplement_freq_list.append(univ_supplement_freq_count)
            univ_fail_freq_list.append(univ_fail_freq_count)

    univ_pass_freq_list = univ_pass_freq_list[:25]
    univ_supplement_freq_list = univ_supplement_freq_list[:25]
    univ_fail_freq_list = univ_fail_freq_list[:25]

    context = {
        'entrance_year_item': entrance_year_qs,
        'current_entrance_year': entrance_year_query,

        'student_region_list': student_region_list,
        'student_region_freq_list': student_region_freq_list,
        'current_region': student_region_query,

        'univ_name_list': univ_name_list,
        'univ_freq_list': univ_freq_list,

        'univ_pass_freq_list': univ_pass_freq_list,
        'univ_supplement_freq_list': univ_supplement_freq_list,
        'univ_fail_freq_list': univ_fail_freq_list,
    }
    return render(request, template, context)


@login_required(login_url="login")
def grade(request):
    template = "statistic/grade.html"

    # 등급별 사례수
    entrance_year_qs = Student.objects.values('entrance_year').order_by('entrance_year').distinct()
    major_group_qs = MajorGroup.objects.order_by('major_group').distinct()
    admission1_qs = Admission1.objects.values('admission1').order_by('admission1').distinct()

    context = {
        'entrance_year_item': entrance_year_qs,
        'major_group_item': major_group_qs,
        'admission1_item': admission1_qs,
    }
    return render(request, template, context)


@login_required(login_url="login")
def grade_result(request):
    template = "statistic/grade_result.html"

    # 등급별 사례수
    entrance_year_qs = Student.objects.values('entrance_year').order_by('entrance_year').distinct()
    major_group_qs = MajorGroup.objects.order_by('major_group').distinct()
    admission1_qs = Admission1.objects.values('admission1').order_by('admission1').distinct()

    entrance_year_query = request.GET.get('entrance_year')
    major_group_query = request.GET.get('major_group')
    admission1_query = request.GET.get('admission1')
    gte_query = request.GET.get('gte')
    lt_query = request.GET.get('lt')

    grade_list = []
    grade_freq_list = []

    if MajorGroup.objects.get(pk=major_group_query) == '자연':
        grade_freq_qs = Student.objects\
            .filter(entrance_year=entrance_year_query) \
            .filter(major_group=major_group_query) \
            .filter(admission1__admission1__contains=admission1_query)\
            .values_list(Floor('ko_en_math_sci_100'))\
            .annotate(student_grade_count=Count(Floor('ko_en_math_sci_100')))\
            .order_by(Floor('ko_en_math_sci_100'))
    elif MajorGroup.objects.get(pk=major_group_query) == '공통':
        grade_freq_qs = Student.objects \
            .filter(entrance_year=entrance_year_query) \
            .filter(major_group=major_group_query) \
            .filter(admission1__admission1__contains=admission1_query) \
            .values_list(Floor('ko_en_math_soc_sci_100')) \
            .annotate(student_grade_count=Count(Floor('ko_en_math_soc_sci_100'))) \
            .order_by(Floor('ko_en_math_soc_sci_100'))
    else:
        grade_freq_qs = Student.objects \
            .filter(entrance_year=entrance_year_query) \
            .filter(major_group=major_group_query) \
            .filter(admission1__admission1__contains=admission1_query) \
            .values_list(Floor('ko_en_math_soc_100')) \
            .annotate(student_grade_count=Count(Floor('ko_en_math_soc_100'))) \
            .order_by(Floor('ko_en_math_soc_100'))

    for grade in grade_freq_qs:
        grade_list.append(int(grade[0]))
        grade_freq_list.append(grade[1])

    # 등급별 학생 지원대학 현황
    univ_name_list = []
    univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    if MajorGroup.objects.get(pk=major_group_query) == '자연':
        univ_freq_qs = Student.objects\
                           .filter(entrance_year=entrance_year_query) \
                           .filter(major_group=major_group_query) \
                           .filter(admission1__admission1__contains=admission1_query) \
                           .filter(ko_en_math_sci_100__gte=gte_query) \
                           .filter(ko_en_math_sci_100__lt=lt_query)\
                           .values_list('univ_name')\
                           .annotate(univ_count=Count('univ_name'))\
                           .order_by('-univ_count')[:25]
    elif MajorGroup.objects.get(pk=major_group_query) == '공통':
        univ_freq_qs = Student.objects\
                           .filter(entrance_year=entrance_year_query) \
                           .filter(major_group=major_group_query) \
                           .filter(admission1__admission1__contains=admission1_query) \
                           .filter(ko_en_math_soc_sci_100__gte=gte_query) \
                           .filter(ko_en_math_soc_sci_100__lt=lt_query) \
                           .values_list('univ_name') \
                           .annotate(univ_count=Count('univ_name')) \
                           .order_by('-univ_count')[:25]
    else:
        univ_freq_qs = Student.objects\
                           .filter(entrance_year=entrance_year_query) \
                           .filter(major_group=major_group_query) \
                           .filter(admission1__admission1__contains=admission1_query) \
                           .filter(ko_en_math_soc_100__gte=gte_query) \
                           .filter(ko_en_math_soc_100__lt=lt_query) \
                           .values_list('univ_name') \
                           .annotate(univ_count=Count('univ_name')) \
                           .order_by('-univ_count')[:25]

    for univ in univ_freq_qs:
        univ_name = univ_name_qs.get(pk=univ[0])
        univ_name_list.append(univ_name.univ_name)
        univ_freq_list.append(univ[1])

    # 등급별 지원대학 합격/불합격 인원
    univ_pass_freq_list = []
    univ_supplement_freq_list = []
    univ_fail_freq_list = []

    for univ in univ_name_list:
        univ_name = univ_name_qs.get(univ_name=univ)

        if MajorGroup.objects.get(pk=major_group_query) == '자연':
            univ_pass_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(major_group=major_group_query) \
                .filter(admission1__admission1__contains=admission1_query) \
                .filter(univ_name=univ_name.id)\
                .filter(ko_en_math_sci_100__gte=gte_query)\
                .filter(ko_en_math_sci_100__lt=lt_query)\
                .filter(final_step='합격')\
                .count()
            univ_supplement_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(major_group=major_group_query) \
                .filter(admission1__admission1__contains=admission1_query) \
                .filter(univ_name=univ_name.id) \
                .filter(ko_en_math_sci_100__gte=gte_query) \
                .filter(ko_en_math_sci_100__lt=lt_query) \
                .filter(final_step='충원합격') \
                .count()
            univ_fail_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(major_group=major_group_query) \
                .filter(admission1__admission1__contains=admission1_query) \
                .filter(univ_name=univ_name.id) \
                .filter(ko_en_math_sci_100__gte=gte_query) \
                .filter(ko_en_math_sci_100__lt=lt_query) \
                .filter(final_step='불합격') \
                .count()
        elif MajorGroup.objects.get(pk=major_group_query) == '공통':
            univ_pass_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(major_group=major_group_query) \
                .filter(admission1__admission1__contains=admission1_query) \
                .filter(univ_name=univ_name.id)\
                .filter(ko_en_math_soc_sci_100__gte=gte_query) \
                .filter(ko_en_math_soc_sci_100__lt=lt_query) \
                .filter(final_step='합격') \
                .count()
            univ_supplement_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(major_group=major_group_query) \
                .filter(admission1__admission1__contains=admission1_query) \
                .filter(univ_name=univ_name.id) \
                .filter(ko_en_math_soc_sci_100__gte=gte_query) \
                .filter(ko_en_math_soc_sci_100__lt=lt_query) \
                .filter(final_step='충원합격') \
                .count()
            univ_fail_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(major_group=major_group_query) \
                .filter(admission1__admission1__contains=admission1_query) \
                .filter(univ_name=univ_name.id) \
                .filter(ko_en_math_soc_sci_100__gte=gte_query) \
                .filter(ko_en_math_soc_sci_100__lt=lt_query) \
                .filter(final_step='불합격') \
                .count()
        else:
            univ_pass_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(major_group=major_group_query) \
                .filter(admission1__admission1__contains=admission1_query) \
                .filter(univ_name=univ_name.id)\
                .filter(ko_en_math_soc_100__gte=gte_query) \
                .filter(ko_en_math_soc_100__lt=lt_query) \
                .filter(final_step='합격') \
                .count()
            univ_supplement_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(major_group=major_group_query) \
                .filter(admission1__admission1__contains=admission1_query) \
                .filter(univ_name=univ_name.id) \
                .filter(ko_en_math_soc_100__gte=gte_query) \
                .filter(ko_en_math_soc_100__lt=lt_query) \
                .filter(final_step='충원합격') \
                .count()
            univ_fail_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(major_group=major_group_query) \
                .filter(admission1__admission1__contains=admission1_query) \
                .filter(univ_name=univ_name.id) \
                .filter(ko_en_math_soc_100__gte=gte_query) \
                .filter(ko_en_math_soc_100__lt=lt_query) \
                .filter(final_step='불합격') \
                .count()

        univ_pass_freq_list.append(univ_pass_freq_count)
        univ_supplement_freq_list.append(univ_supplement_freq_count)
        univ_fail_freq_list.append(univ_fail_freq_count)

    univ_pass_freq_list = univ_pass_freq_list[:25]
    univ_supplement_freq_list = univ_supplement_freq_list[:25]
    univ_fail_freq_list = univ_fail_freq_list[:25]

    #Chart size
    if len(univ_freq_list) != 0:
        chart_height = (len(univ_freq_list)) * 3 + 6
    else:
        chart_height = 6

    context = {
        'entrance_year_item': entrance_year_qs,
        'major_group_item': major_group_qs,
        'admission1_item': admission1_qs,

        'current_entrance_year': entrance_year_query,
        'current_major_group': int(major_group_query),
        'current_admission1': admission1_query,
        'current_gte': int(gte_query),

        'grade_list': grade_list,
        'grade_freq_list': grade_freq_list,

        'univ_name_list': univ_name_list,
        'univ_freq_list': univ_freq_list,

        'univ_pass_freq_list': univ_pass_freq_list,
        'univ_supplement_freq_list': univ_supplement_freq_list,
        'univ_fail_freq_list': univ_fail_freq_list,

        'chart_height': chart_height,
    }
    return render(request, template, context)


@login_required(login_url="login")
def admission1(request):
    template = "statistic/admission1.html"

    entrance_year_qs = Student.objects.values('entrance_year').order_by('entrance_year').distinct()
    major_group_qs = MajorGroup.objects.order_by('major_group').distinct()
    univ_region_qs = UnivRegion.objects.order_by('univ_region').distinct()

    context = {
        'entrance_year_item': entrance_year_qs,
        'major_group_item': major_group_qs,
        'univ_region_item': univ_region_qs,
    }
    return render(request, template, context)


@login_required(login_url="login")
def admission1_result(request):
    template = "statistic/admission1_result.html"

    entrance_year_qs = Student.objects.values('entrance_year').order_by('entrance_year').distinct()
    major_group_qs = MajorGroup.objects.order_by('major_group').distinct()
    univ_region_qs = UnivRegion.objects.order_by('univ_region').distinct()
    admission1_qs = Admission1.objects.values('admission1').order_by('admission1').distinct()

    entrance_year_query = request.GET.get('entrance_year')
    major_group_query = request.GET.get('major_group')
    univ_region_query = request.GET.get('univ_region')
    admission1_query = request.GET.get('admission1')

    # 전형요소 별 지원 인원
    admission1_list = []
    admission1_freq_list = []

    for admission1 in admission1_qs:
        admission1 = list(admission1.values())[0]
        admission1_freq = Student.objects \
            .filter(entrance_year=entrance_year_query) \
            .filter(major_group=major_group_query) \
            .filter(univ_region=univ_region_query) \
            .filter(admission1__admission1__contains=admission1)\
            .count()
        admission1_list.append(admission1)
        admission1_freq_list.append(admission1_freq)

    # 등급별 학생 지원대학 현황
    univ_name_list = []
    univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    if admission1_query == '교과':
        univ_freq_qs = Student.objects \
                           .filter(entrance_year=entrance_year_query) \
                           .filter(major_group=major_group_query) \
                           .filter(univ_region=univ_region_query) \
                           .filter(admission1__admission1__contains=admission1_query) \
                           .values_list('univ_name') \
                           .annotate(univ_count=Count('univ_name')) \
                           .order_by('-univ_count')[:25]
    elif admission1_query == '종합':
        univ_freq_qs = Student.objects \
                           .filter(entrance_year=entrance_year_query) \
                           .filter(major_group=major_group_query) \
                           .filter(univ_region=univ_region_query) \
                           .filter(admission1__admission1__contains=admission1_query) \
                           .values_list('univ_name') \
                           .annotate(univ_count=Count('univ_name')) \
                           .order_by('-univ_count')[:25]
    elif admission1_query == '논술':
        univ_freq_qs = Student.objects \
                           .filter(entrance_year=entrance_year_query) \
                           .filter(major_group=major_group_query) \
                           .filter(univ_region=univ_region_query) \
                           .filter(admission1__admission1__contains=admission1_query) \
                           .values_list('univ_name') \
                           .annotate(univ_count=Count('univ_name')) \
                           .order_by('-univ_count')[:25]
    else:
        univ_freq_qs = Student.objects \
                           .filter(entrance_year=entrance_year_query) \
                           .filter(major_group=major_group_query) \
                           .filter(univ_region=univ_region_query) \
                           .filter(admission1__admission1__contains=admission1_query) \
                           .values_list('univ_name') \
                           .annotate(univ_count=Count('univ_name')) \
                           .order_by('-univ_count')[:25]

    for univ in univ_freq_qs:
        univ_name = univ_name_qs.get(pk=univ[0])
        univ_name_list.append(univ_name.univ_name)
        univ_freq_list.append(univ[1])

    # 전형별 지원대학 합격/불합격 인원
    univ_pass_freq_list = []
    univ_supplement_freq_list = []
    univ_fail_freq_list = []

    for univ in univ_name_list:
        univ_name = univ_name_qs.get(univ_name=univ)

        univ_pass_freq_count = Student.objects \
            .filter(entrance_year=entrance_year_query) \
            .filter(major_group=major_group_query) \
            .filter(univ_region=univ_region_query) \
            .filter(admission1__admission1__contains=admission1_query) \
            .filter(univ_name=univ_name.id) \
            .filter(final_step='합격') \
            .count()
        univ_supplement_freq_count = Student.objects \
            .filter(entrance_year=entrance_year_query) \
            .filter(major_group=major_group_query) \
            .filter(univ_region=univ_region_query) \
            .filter(admission1__admission1__contains=admission1_query) \
            .filter(univ_name=univ_name.id) \
            .filter(final_step='충원합격') \
            .count()
        univ_fail_freq_count = Student.objects \
            .filter(entrance_year=entrance_year_query) \
            .filter(major_group=major_group_query) \
            .filter(univ_region=univ_region_query) \
            .filter(admission1__admission1__contains=admission1_query) \
            .filter(univ_name=univ_name.id) \
            .filter(final_step='불합격') \
            .count()

        univ_pass_freq_list.append(univ_pass_freq_count)
        univ_supplement_freq_list.append(univ_supplement_freq_count)
        univ_fail_freq_list.append(univ_fail_freq_count)

    univ_pass_freq_list = univ_pass_freq_list[:25]
    univ_supplement_freq_list = univ_supplement_freq_list[:25]
    univ_fail_freq_list = univ_fail_freq_list[:25]

    #Chart size
    if len(univ_freq_list) != 0:
        chart_height = (len(univ_freq_list)) * 3 + 6
    else:
        chart_height = 6

    context = {
        'entrance_year_item': entrance_year_qs,
        'major_group_item': major_group_qs,
        'univ_region_item': univ_region_qs,

        'current_entrance_year': int(entrance_year_query),
        'current_major_group': int(major_group_query),
        'current_univ_region': int(univ_region_query),
        'current_admission1': admission1_query,

        'admission1_list': admission1_list,
        'admission1_freq_list': admission1_freq_list,

        'univ_name_list': univ_name_list,
        'univ_freq_list': univ_freq_list,

        'univ_pass_freq_list': univ_pass_freq_list,
        'univ_supplement_freq_list': univ_supplement_freq_list,
        'univ_fail_freq_list': univ_fail_freq_list,

        'chart_height': chart_height,
    }
    return render(request, template, context)


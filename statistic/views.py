from django.shortcuts import render
from analysis.models import *
from django.db.models import Count, Avg
from django.db.models.functions import Floor
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def static_student_region(request):
    template = "statistic/static_student_region.html"

    # 지역별 사례수
    entrance_year_qs = Student.objects.values('entrance_year').order_by('entrance_year').distinct()

    context = {
        'entrance_year_item': entrance_year_qs,
    }
    return render(request, template, context)


@login_required(login_url="login")
def static_student_region_result(request):
    template = "statistic/static_student_region_result.html"

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
    app_univ_name_list = []
    app_univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    if student_region_query == '충청도':
        app_univ_freq_qs = Student.objects\
                               .filter(entrance_year=entrance_year_query)\
                               .values_list('univ_name')\
                               .annotate(univ_count=Count('univ_name'))\
                               .order_by('-univ_count')[:25]
    else:
        app_univ_freq_qs = Student.objects \
                               .filter(entrance_year=entrance_year_query) \
                               .filter(student_region=student_region_query) \
                               .values_list('univ_name') \
                               .annotate(univ_count=Count('univ_name')) \
                               .order_by('-univ_count')[:25]

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    # 지역별 지원대학 합격/불합격 인원
    app_univ_pass_freq_list = []
    app_univ_fail_freq_list = []

    if student_region_query == '충청도':
        for univ in app_univ_name_list:
            app_univ_name = univ_name_qs.get(univ_name=univ)
            app_univ_pass_freq_count = Student.objects\
                .filter(entrance_year=entrance_year_query)\
                .filter(univ_name=app_univ_name.id) \
                .filter(Q(final_step='합격') | Q(final_step='충원합격')) \
                .count()
            app_univ_fail_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(univ_name=app_univ_name.id) \
                .filter(final_step='불합격') \
                .count()
            app_univ_pass_freq_list.append(app_univ_pass_freq_count)
            app_univ_fail_freq_list.append(app_univ_fail_freq_count)

    else:
        for univ in app_univ_name_list:
            app_univ_name = univ_name_qs.get(univ_name=univ)
            app_univ_pass_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(student_region=student_region_query)\
                .filter(univ_name=app_univ_name.id) \
                .filter(Q(final_step='합격') | Q(final_step='충원합격')) \
                .count()
            app_univ_fail_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(student_region=student_region_query)\
                .filter(univ_name=app_univ_name.id) \
                .filter(final_step='불합격') \
                .count()
            app_univ_pass_freq_list.append(app_univ_pass_freq_count)
            app_univ_fail_freq_list.append(app_univ_fail_freq_count)

    app_univ_pass_freq_list = app_univ_pass_freq_list[:25]
    app_univ_fail_freq_list = app_univ_fail_freq_list[:25]

    context = {
        'entrance_year_item': entrance_year_qs,
        'current_entrance_year': entrance_year_query,

        'student_region_list': student_region_list,
        'student_region_freq_list': student_region_freq_list,
        'current_region': student_region_query,

        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,

        'app_univ_pass_freq_list': app_univ_pass_freq_list,
        'app_univ_fail_freq_list': app_univ_fail_freq_list,
    }
    return render(request, template, context)


@login_required(login_url="login")
def static_grade(request):
    template = "statistic/static_grade.html"

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
def static_grade_result(request):
    template = "statistic/static_grade_result.html"

    # 등급별 사례수
    entrance_year_qs = Student.objects.values('entrance_year').order_by('entrance_year').distinct()
    major_group_qs = MajorGroup.objects.order_by('major_group').distinct()
    admission1_qs = Admission1.objects.values('admission1').order_by('admission1').distinct()

    entrance_year_query = request.GET.get('entrance_year')
    major_group_query = request.GET.get('major_group')
    admission1_query = request.GET.get('admission1')
    gte_query = request.GET.get('gte')
    lt_query = request.GET.get('lt')

    student_grade_list = []
    student_grade_freq_list = []

    if MajorGroup.objects.get(pk=major_group_query) == '자연':
        student_grade_freq_qs = Student.objects \
            .filter(entrance_year=entrance_year_query) \
            .filter(major_group=major_group_query) \
            .filter(admission1__admission1__contains=admission1_query)\
            .values_list(Floor('ko_en_math_sci_100'))\
            .annotate(student_grade_count=Count(Floor('ko_en_math_sci_100')))\
            .order_by(Floor('ko_en_math_sci_100'))
    elif MajorGroup.objects.get(pk=major_group_query) == '공통':
        student_grade_freq_qs = Student.objects \
            .filter(entrance_year=entrance_year_query) \
            .filter(major_group=major_group_query) \
            .filter(admission1__admission1__contains=admission1_query) \
            .values_list(Floor('ko_en_math_soc_sci_100')) \
            .annotate(student_grade_count=Count(Floor('ko_en_math_soc_sci_100'))) \
            .order_by(Floor('ko_en_math_soc_sci_100'))
    else:
        student_grade_freq_qs = Student.objects \
            .filter(entrance_year=entrance_year_query) \
            .filter(major_group=major_group_query) \
            .filter(admission1__admission1__contains=admission1_query) \
            .values_list(Floor('ko_en_math_soc_100')) \
            .annotate(student_grade_count=Count(Floor('ko_en_math_soc_100'))) \
            .order_by(Floor('ko_en_math_soc_100'))

    for student_grade in student_grade_freq_qs:
        student_grade_list.append(int(student_grade[0]))
        student_grade_freq_list.append(student_grade[1])

    # 1등급대 학생 지원대학 현황
    app_univ_name_list = []
    app_univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    if MajorGroup.objects.get(pk=major_group_query) == '자연':
        app_univ_freq_qs = Student.objects \
                               .filter(entrance_year=entrance_year_query) \
                               .filter(major_group=major_group_query) \
                               .filter(admission1__admission1__contains=admission1_query) \
                               .filter(ko_en_math_sci_100__gte=gte_query) \
                               .filter(ko_en_math_sci_100__lt=lt_query)\
                               .values_list('univ_name')\
                               .annotate(univ_count=Count('univ_name'))\
                               .order_by('-univ_count')[:25]
    elif MajorGroup.objects.get(pk=major_group_query) == '공통':
        app_univ_freq_qs = Student.objects \
                               .filter(entrance_year=entrance_year_query) \
                               .filter(major_group=major_group_query) \
                               .filter(admission1__admission1__contains=admission1_query) \
                               .filter(ko_en_math_soc_sci_100__gte=gte_query) \
                               .filter(ko_en_math_soc_sci_100__lt=lt_query) \
                               .values_list('univ_name') \
                               .annotate(univ_count=Count('univ_name')) \
                               .order_by('-univ_count')[:25]
    else:
        app_univ_freq_qs = Student.objects \
                               .filter(entrance_year=entrance_year_query) \
                               .filter(major_group=major_group_query) \
                               .filter(admission1__admission1__contains=admission1_query) \
                               .filter(ko_en_math_soc_100__gte=gte_query) \
                               .filter(ko_en_math_soc_100__lt=lt_query) \
                               .values_list('univ_name') \
                               .annotate(univ_count=Count('univ_name')) \
                               .order_by('-univ_count')[:25]

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    # 등급별 지원대학 합격/불합격 인원
    app_univ_pass_freq_list = []
    app_univ_fail_freq_list = []

    for univ in app_univ_name_list:
        app_univ_name = univ_name_qs.get(univ_name=univ)

        if MajorGroup.objects.get(pk=major_group_query) == '자연':
            app_univ_pass_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(major_group=major_group_query) \
                .filter(admission1__admission1__contains=admission1_query) \
                .filter(univ_name=app_univ_name.id)\
                .filter(ko_en_math_sci_100__gte=gte_query)\
                .filter(ko_en_math_sci_100__lt=lt_query)\
                .filter(Q(final_step='합격') | Q(final_step='충원합격'))\
                .count()
        elif MajorGroup.objects.get(pk=major_group_query) == '공통':
            app_univ_pass_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(major_group=major_group_query) \
                .filter(admission1__admission1__contains=admission1_query) \
                .filter(univ_name=app_univ_name.id)\
                .filter(ko_en_math_soc_sci_100__gte=gte_query) \
                .filter(ko_en_math_soc_sci_100__lt=lt_query) \
                .filter(Q(final_step='합격') | Q(final_step='충원합격')) \
                .count()
        else:
            app_univ_pass_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(major_group=major_group_query) \
                .filter(admission1__admission1__contains=admission1_query) \
                .filter(univ_name=app_univ_name.id)\
                .filter(ko_en_math_soc_100__gte=gte_query) \
                .filter(ko_en_math_soc_100__lt=lt_query) \
                .filter(Q(final_step='합격') | Q(final_step='충원합격')) \
                .count()

        if MajorGroup.objects.get(pk=major_group_query) == '자연':
            app_univ_fail_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(major_group=major_group_query) \
                .filter(admission1__admission1__contains=admission1_query) \
                .filter(univ_name=app_univ_name.id)\
                .filter(ko_en_math_sci_100__gte=gte_query)\
                .filter(ko_en_math_sci_100__lt=lt_query)\
                .filter(final_step='불합격') \
                .count()
        elif MajorGroup.objects.get(pk=major_group_query) == '공통':
            app_univ_fail_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(major_group=major_group_query) \
                .filter(admission1__admission1__contains=admission1_query) \
                .filter(univ_name=app_univ_name.id)\
                .filter(ko_en_math_soc_sci_100__gte=gte_query) \
                .filter(ko_en_math_soc_sci_100__lt=lt_query) \
                .filter(final_step='불합격') \
                .count()
        else:
            app_univ_fail_freq_count = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(major_group=major_group_query) \
                .filter(admission1__admission1__contains=admission1_query) \
                .filter(univ_name=app_univ_name.id)\
                .filter(ko_en_math_soc_100__gte=gte_query) \
                .filter(ko_en_math_soc_100__lt=lt_query) \
                .filter(final_step='불합격') \
                .count()

        app_univ_pass_freq_list.append(app_univ_pass_freq_count)
        app_univ_fail_freq_list.append(app_univ_fail_freq_count)

    app_univ_pass_freq_list = app_univ_pass_freq_list[:25]
    app_univ_fail_freq_list = app_univ_fail_freq_list[:25]

    if len(app_univ_freq_list) != 0:
        if max(app_univ_freq_list) < 5:
            chart_width = 70
            chart_height = (len(app_univ_freq_list) + 1) * 3
        elif max(app_univ_freq_list) < 10:
            chart_width = 80
            chart_height = (len(app_univ_freq_list) + 1) * 3
        else:
            chart_width = (max(app_univ_freq_list) // 10 + 70)
            chart_height = (len(app_univ_freq_list) + 1) * 3
    else:
        chart_width = 10
        chart_height = 1

    context = {
        'entrance_year_item': entrance_year_qs,
        'major_group_item': major_group_qs,
        'admission1_item': admission1_qs,

        'current_entrance_year': entrance_year_query,
        'current_major_group': int(major_group_query),
        'current_admission1': admission1_query,
        'current_gte': int(gte_query),

        'student_grade_list': student_grade_list,
        'student_grade_freq_list': student_grade_freq_list,

        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,

        'chart_width': chart_width,
        'chart_height': chart_height,

        'app_univ_pass_freq_list': app_univ_pass_freq_list,
        'app_univ_fail_freq_list': app_univ_fail_freq_list,
    }
    return render(request, template, context)


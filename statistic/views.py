from django.shortcuts import render
from analysis.models import *
from django.db.models import Count
from django.db.models.functions import Floor
from django.db.models import Q


def app_region(request):
    template = "statistic/app_region.html"

    # 지역별 사례수
    student_region_freq_qs = Student.objects.values_list('student_region')\
        .annotate(student_region_count=Count('student_region'))\
        .order_by('-student_region_count')
    student_region_list = []
    student_region_freq_list = []

    for student_region in student_region_freq_qs:
        student_region_list.append(student_region[0])
        student_region_freq_list.append(student_region[1])

    # 충청도지역 학생 지원대학 현황
    univ_name_qs = UnivName.objects.all()

    app_cc_sum = Student.objects.all().count()
    app_univ_freq_qs = Student.objects.values_list('univ_name')\
                                      .annotate(univ_count=Count('univ_name'))\
                                      .order_by('-univ_count')[:25]
    app_univ_name_list = []
    app_univ_freq_list = []

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    context = {
        'student_region_list': student_region_list,
        'student_region_freq_list': student_region_freq_list,

        'app_cc_sum': app_cc_sum,
        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,

    }
    return render(request, template, context)


def app_region_tab_dj(request):
    template = "statistic/app_region_tab.html"

    univ_name_qs = UnivName.objects.all()

    # 지역별 사례수
    student_region_freq_qs = Student.objects.values_list('student_region')\
        .annotate(student_region_count=Count('student_region'))\
        .order_by('-student_region_count')
    student_region_list = []
    student_region_freq_list = []

    for student_region in student_region_freq_qs:
        student_region_list.append(student_region[0])
        student_region_freq_list.append(student_region[1])

    # 대전지역 학생 지원대학 현황
    app_dj_sum = Student.objects.filter(student_region='대전').count()
    app_univ_freq_qs = Student.objects.filter(student_region='대전')\
                                      .values_list('univ_name')\
                                      .annotate(univ_count=Count('univ_name'))\
                                      .order_by('-univ_count')[:25]
    app_univ_name_list = []
    app_univ_freq_list = []

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    context = {
        'student_region_list': student_region_list,
        'student_region_freq_list': student_region_freq_list,

        'app_dj_sum': app_dj_sum,
        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,
    }
    return render(request, template, context)


def app_region_tab_sj(request):
    template = "statistic/app_region_tab.html"

    # 지역별 사례수
    student_region_freq_qs = Student.objects.values_list('student_region')\
        .annotate(student_region_count=Count('student_region'))\
        .order_by('-student_region_count')
    student_region_list = []
    student_region_freq_list = []

    for student_region in student_region_freq_qs:
        student_region_list.append(student_region[0])
        student_region_freq_list.append(student_region[1])

    univ_name_qs = UnivName.objects.all()

    # 세종지역 학생 지원대학 현황
    app_sj_sum = Student.objects.filter(student_region='세종').count()
    app_univ_freq_qs = Student.objects.filter(student_region='세종')\
                                      .values_list('univ_name').annotate(univ_count=Count('univ_name'))\
                                      .order_by('-univ_count')[:25]
    app_univ_name_list = []
    app_univ_freq_list = []

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    context = {
        'student_region_list': student_region_list,
        'student_region_freq_list': student_region_freq_list,

        'app_sj_sum': app_sj_sum,
        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,
    }
    return render(request, template, context)


def app_region_tab_cn(request):
    template = "statistic/app_region_tab.html"

    # 지역별 사례수
    student_region_freq_qs = Student.objects.values_list('student_region')\
        .annotate(student_region_count=Count('student_region'))\
        .order_by('-student_region_count')
    student_region_list = []
    student_region_freq_list = []

    for student_region in student_region_freq_qs:
        student_region_list.append(student_region[0])
        student_region_freq_list.append(student_region[1])

    univ_name_qs = UnivName.objects.all()

    # 충남지역 학생 지원대학 현황
    app_cn_sum = Student.objects.filter(student_region='충남').count()
    app_univ_freq_qs = Student.objects.filter(student_region='충남')\
                              .values_list('univ_name')\
                              .annotate(univ_count=Count('univ_name'))\
                              .order_by('-univ_count')[:25]
    app_univ_name_list = []
    app_univ_freq_list = []

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    context = {
        'student_region_list': student_region_list,
        'student_region_freq_list': student_region_freq_list,

        'app_cn_sum': app_cn_sum,
        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,
    }
    return render(request, template, context)


def app_region_tab_cb(request):
    template = "statistic/app_region_tab.html"

    # 지역별 사례수
    student_region_freq_qs = Student.objects.values_list('student_region')\
        .annotate(student_region_count=Count('student_region'))\
        .order_by('-student_region_count')
    student_region_list = []
    student_region_freq_list = []

    for student_region in student_region_freq_qs:
        student_region_list.append(student_region[0])
        student_region_freq_list.append(student_region[1])

    univ_name_qs = UnivName.objects.all()

    # 충북지역 학생 지원대학 현황
    app_cb_sum = Student.objects.filter(student_region='충북').count()
    app_univ_freq_qs = Student.objects.filter(student_region='충북')\
                                      .values_list('univ_name')\
                                      .annotate(univ_count=Count('univ_name'))\
                                      .order_by('-univ_count')[:25]
    app_univ_name_list = []
    app_univ_freq_list = []

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    context = {
        'student_region_list': student_region_list,
        'student_region_freq_list': student_region_freq_list,

        'app_cb_sum': app_cb_sum,
        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,
    }
    return render(request, template, context)


def app_grade_in(request):
    template = "statistic/app_grade_in.html"

    # 등급별 사례수
    student_grade_in_list = []
    student_grade_in_freq_list = []

    student_grade_freq_qs = Student.objects.filter(major_group=2)\
        .values_list(Floor('ko_en_math_soc_100'))\
        .annotate(student_grade_count=Count(Floor('ko_en_math_soc_100')))\
        .order_by(Floor('ko_en_math_soc_100'))

    for student_grade in student_grade_freq_qs:
        student_grade_in_list.append(int(student_grade[0]))
        student_grade_in_freq_list.append(student_grade[1])

    # 인문 1등급대 학생 지원대학 현황
    app_univ_name_list = []
    app_univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    app_univ_freq_qs = Student.objects.filter(major_group=2)\
                                     .filter(ko_en_math_soc_100__lt=2)\
                                     .values_list('univ_name')\
                                     .annotate(univ_count=Count('univ_name'))\
                                     .order_by('-univ_count')[:25]

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    # 인문 1등급대 학생 지원대학 합격/불합격 인원
    app_univ_pass_freq_list = []
    app_univ_fail_freq_list = []

    for univ in app_univ_name_list:
        app_univ_name = univ_name_qs.get(univ_name=univ)
        app_univ_pass_freq_count = Student.objects.filter(major_group=2) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_soc_100__gte=1)\
            .filter(ko_en_math_soc_100__lt=2)\
            .filter(Q(final_step='합격') | Q(final_step='충원합격'))\
            .count()
        app_univ_fail_freq_count = Student.objects.filter(major_group=2)\
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_soc_100__gte=1) \
            .filter(ko_en_math_soc_100__lt=2) \
            .filter(final_step='불합격') \
            .count()
        app_univ_pass_freq_list.append(app_univ_pass_freq_count)
        app_univ_fail_freq_list.append(app_univ_fail_freq_count)

        app_univ_pass_freq_list = app_univ_pass_freq_list[:25]
        app_univ_fail_freq_list = app_univ_fail_freq_list[:25]

    context = {
        'student_grade_in_list': student_grade_in_list,
        'student_grade_in_freq_list': student_grade_in_freq_list,

        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,

        'app_univ_pass_freq_list': app_univ_pass_freq_list,
        'app_univ_fail_freq_list': app_univ_fail_freq_list,
    }
    return render(request, template, context)


def app_grade_in_tab_2(request):
    template = "statistic/app_grade_in_tab.html"

    # 등급별 사례수
    student_grade_in_list = []
    student_grade_in_freq_list = []
    student_grade_freq_qs = Student.objects.filter(major_group=2)\
        .values_list(Floor('ko_en_math_soc_100'))\
        .annotate(student_grade_count=Count(Floor('ko_en_math_soc_100')))\
        .order_by(Floor('ko_en_math_soc_100'))

    for student_grade in student_grade_freq_qs:
        student_grade_in_list.append(int(student_grade[0]))
        student_grade_in_freq_list.append(student_grade[1])

    # 인문 2등급대 학생 지원대학 현황
    app_univ_name_list = []
    app_univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    app_univ_freq_qs = Student.objects.filter(major_group=2)\
                                     .filter(ko_en_math_soc_100__gte=2)\
                                     .filter(ko_en_math_soc_100__lt=3)\
                                     .values_list('univ_name')\
                                     .annotate(univ_count=Count('univ_name'))\
                                     .order_by('-univ_count')[:25]
    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    # 인문 2등급대 학생 지원대학 합격/불합격 인원
    app_univ_pass_freq_list = []
    app_univ_fail_freq_list = []

    for univ in app_univ_name_list:
        app_univ_name = univ_name_qs.get(univ_name=univ)
        app_univ_pass_freq_count = Student.objects.filter(major_group=2) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_soc_100__gte=2) \
            .filter(ko_en_math_soc_100__lt=3) \
            .filter(Q(final_step='합격') | Q(final_step='충원합격')) \
            .count()
        app_univ_fail_freq_count = Student.objects.filter(major_group=2) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_soc_100__gte=2) \
            .filter(ko_en_math_soc_100__lt=3) \
            .filter(final_step='불합격') \
            .count()
        app_univ_pass_freq_list.append(app_univ_pass_freq_count)
        app_univ_fail_freq_list.append(app_univ_fail_freq_count)

        app_univ_pass_freq_list = app_univ_pass_freq_list[:25]
        app_univ_fail_freq_list = app_univ_fail_freq_list[:25]

    context = {
        'student_grade_in_list': student_grade_in_list,
        'student_grade_in_freq_list': student_grade_in_freq_list,

        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,

        'app_univ_pass_freq_list': app_univ_pass_freq_list,
        'app_univ_fail_freq_list': app_univ_fail_freq_list,
    }
    return render(request, template, context)


def app_grade_in_tab_3(request):
    template = "statistic/app_grade_in_tab.html"

    # 등급별 사례수
    student_grade_in_list = []
    student_grade_in_freq_list = []
    student_grade_freq_qs = Student.objects.filter(major_group=2) \
        .values_list(Floor('ko_en_math_soc_100')) \
        .annotate(student_grade_count=Count(Floor('ko_en_math_soc_100'))) \
        .order_by(Floor('ko_en_math_soc_100'))

    for student_grade in student_grade_freq_qs:
        student_grade_in_list.append(int(student_grade[0]))
        student_grade_in_freq_list.append(student_grade[1])

    # 인문 3등급대 학생 지원대학 현황
    app_univ_name_list = []
    app_univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    app_univ_freq_qs = Student.objects.filter(major_group=2)\
                                     .filter(ko_en_math_soc_100__gte=3)\
                                     .filter(ko_en_math_soc_100__lt=4)\
                                     .values_list('univ_name')\
                                     .annotate(univ_count=Count('univ_name'))\
                                     .order_by('-univ_count')[:25]

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    # 인문 3등급대 학생 지원대학 합격/불합격 인원
    app_univ_pass_freq_list = []
    app_univ_fail_freq_list = []

    for univ in app_univ_name_list:
        app_univ_name = univ_name_qs.get(univ_name=univ)
        app_univ_pass_freq_count = Student.objects.filter(major_group=2) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_soc_100__gte=3) \
            .filter(ko_en_math_soc_100__lt=4) \
            .filter(Q(final_step='합격') | Q(final_step='충원합격')) \
            .count()
        app_univ_fail_freq_count = Student.objects.filter(major_group=2) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_soc_100__gte=3) \
            .filter(ko_en_math_soc_100__lt=4) \
            .filter(final_step='불합격') \
            .count()
        app_univ_pass_freq_list.append(app_univ_pass_freq_count)
        app_univ_fail_freq_list.append(app_univ_fail_freq_count)

        app_univ_pass_freq_list = app_univ_pass_freq_list[:25]
        app_univ_fail_freq_list = app_univ_fail_freq_list[:25]

    context = {
        'student_grade_in_list': student_grade_in_list,
        'student_grade_in_freq_list': student_grade_in_freq_list,

        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,

        'app_univ_pass_freq_list': app_univ_pass_freq_list,
        'app_univ_fail_freq_list': app_univ_fail_freq_list,
    }
    return render(request, template, context)


def app_grade_in_tab_4(request):
    template = "statistic/app_grade_in_tab.html"

    # 등급별 사례수
    student_grade_in_list = []
    student_grade_in_freq_list = []
    student_grade_freq_qs = Student.objects.filter(major_group=2) \
        .values_list(Floor('ko_en_math_soc_100')) \
        .annotate(student_grade_count=Count(Floor('ko_en_math_soc_100'))) \
        .order_by(Floor('ko_en_math_soc_100'))

    for student_grade in student_grade_freq_qs:
        student_grade_in_list.append(int(student_grade[0]))
        student_grade_in_freq_list.append(student_grade[1])

    # 인문 4등급대 학생 지원대학 현황
    app_univ_name_list = []
    app_univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    app_univ_freq_qs = Student.objects.filter(major_group=2)\
                                     .filter(ko_en_math_soc_100__gte=4)\
                                     .filter(ko_en_math_soc_100__lt=5)\
                                     .values_list('univ_name')\
                                     .annotate(univ_count=Count('univ_name'))\
                                     .order_by('-univ_count')[:25]

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    # 인문 4등급대 학생 지원대학 합격/불합격 인원
    app_univ_pass_freq_list = []
    app_univ_fail_freq_list = []

    for univ in app_univ_name_list:
        app_univ_name = univ_name_qs.get(univ_name=univ)
        app_univ_pass_freq_count = Student.objects.filter(major_group=2) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_soc_100__gte=4) \
            .filter(ko_en_math_soc_100__lt=5) \
            .filter(Q(final_step='합격') | Q(final_step='충원합격')) \
            .count()
        app_univ_fail_freq_count = Student.objects.filter(major_group=2) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_soc_100__gte=4) \
            .filter(ko_en_math_soc_100__lt=5) \
            .filter(final_step='불합격') \
            .count()
        app_univ_pass_freq_list.append(app_univ_pass_freq_count)
        app_univ_fail_freq_list.append(app_univ_fail_freq_count)

        app_univ_pass_freq_list = app_univ_pass_freq_list[:25]
        app_univ_fail_freq_list = app_univ_fail_freq_list[:25]

    context = {
        'student_grade_in_list': student_grade_in_list,
        'student_grade_in_freq_list': student_grade_in_freq_list,

        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,

        'app_univ_pass_freq_list': app_univ_pass_freq_list,
        'app_univ_fail_freq_list': app_univ_fail_freq_list,
    }
    return render(request, template, context)


def app_grade_in_tab_5(request):
    template = "statistic/app_grade_in_tab.html"

    # 등급별 사례수
    student_grade_in_list = []
    student_grade_in_freq_list = []
    student_grade_freq_qs = Student.objects.filter(major_group=2) \
        .values_list(Floor('ko_en_math_soc_100')) \
        .annotate(student_grade_count=Count(Floor('ko_en_math_soc_100'))) \
        .order_by(Floor('ko_en_math_soc_100'))

    for student_grade in student_grade_freq_qs:
        student_grade_in_list.append(int(student_grade[0]))
        student_grade_in_freq_list.append(student_grade[1])

    # 인문 5등급대 학생 지원대학 현황
    app_univ_name_list = []
    app_univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    app_univ_freq_qs = Student.objects.filter(major_group=2)\
                                     .filter(ko_en_math_soc_100__gte=5)\
                                     .filter(ko_en_math_soc_100__lt=6)\
                                     .values_list('univ_name')\
                                     .annotate(univ_count=Count('univ_name'))\
                                     .order_by('-univ_count')[:25]

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    # 인문 5등급대 학생 지원대학 합격/불합격 인원
    app_univ_pass_freq_list = []
    app_univ_fail_freq_list = []

    for univ in app_univ_name_list:
        app_univ_name = univ_name_qs.get(univ_name=univ)
        app_univ_pass_freq_count = Student.objects.filter(major_group=2) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_soc_100__gte=5) \
            .filter(ko_en_math_soc_100__lt=6) \
            .filter(Q(final_step='합격') | Q(final_step='충원합격')) \
            .count()
        app_univ_fail_freq_count = Student.objects.filter(major_group=2) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_soc_100__gte=5) \
            .filter(ko_en_math_soc_100__lt=6) \
            .filter(final_step='불합격') \
            .count()
        app_univ_pass_freq_list.append(app_univ_pass_freq_count)
        app_univ_fail_freq_list.append(app_univ_fail_freq_count)

        app_univ_pass_freq_list = app_univ_pass_freq_list[:25]
        app_univ_fail_freq_list = app_univ_fail_freq_list[:25]

    context = {
        'student_grade_in_list': student_grade_in_list,
        'student_grade_in_freq_list': student_grade_in_freq_list,

        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,

        'app_univ_pass_freq_list': app_univ_pass_freq_list,
        'app_univ_fail_freq_list': app_univ_fail_freq_list,
    }
    return render(request, template, context)


def app_grade_in_tab_6(request):
    template = "statistic/app_grade_in_tab.html"

    # 등급별 사례수
    student_grade_in_list = []
    student_grade_in_freq_list = []
    student_grade_freq_qs = Student.objects.filter(major_group=2) \
        .values_list(Floor('ko_en_math_soc_100')) \
        .annotate(student_grade_count=Count(Floor('ko_en_math_soc_100'))) \
        .order_by(Floor('ko_en_math_soc_100'))

    for student_grade in student_grade_freq_qs:
        student_grade_in_list.append(int(student_grade[0]))
        student_grade_in_freq_list.append(student_grade[1])

    # 인문 6등급대 학생 지원대학 현황
    app_univ_name_list = []
    app_univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    app_univ_freq_qs = Student.objects.filter(major_group=2)\
                                     .filter(ko_en_math_soc_100__gte=6)\
                                     .filter(ko_en_math_soc_100__lt=7)\
                                     .values_list('univ_name')\
                                     .annotate(univ_count=Count('univ_name'))\
                                     .order_by('-univ_count')[:25]

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    # 인문 6등급대 학생 지원대학 합격/불합격 인원
    app_univ_pass_freq_list = []
    app_univ_fail_freq_list = []

    for univ in app_univ_name_list:
        app_univ_name = univ_name_qs.get(univ_name=univ)
        app_univ_pass_freq_count = Student.objects.filter(major_group=2) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_soc_100__gte=6) \
            .filter(ko_en_math_soc_100__lt=7) \
            .filter(Q(final_step='합격') | Q(final_step='충원합격')) \
            .count()
        app_univ_fail_freq_count = Student.objects.filter(major_group=2) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_soc_100__gte=6) \
            .filter(ko_en_math_soc_100__lt=7) \
            .filter(final_step='불합격') \
            .count()
        app_univ_pass_freq_list.append(app_univ_pass_freq_count)
        app_univ_fail_freq_list.append(app_univ_fail_freq_count)

        app_univ_pass_freq_list = app_univ_pass_freq_list[:25]
        app_univ_fail_freq_list = app_univ_fail_freq_list[:25]

    context = {
        'student_grade_in_list': student_grade_in_list,
        'student_grade_in_freq_list': student_grade_in_freq_list,

        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,

        'app_univ_pass_freq_list': app_univ_pass_freq_list,
        'app_univ_fail_freq_list': app_univ_fail_freq_list,
    }
    return render(request, template, context)


def app_grade_in_tab_7(request):
    template = "statistic/app_grade_in_tab.html"

    # 등급별 사례수
    student_grade_in_list = []
    student_grade_in_freq_list = []
    student_grade_freq_qs = Student.objects.filter(major_group=2) \
        .values_list(Floor('ko_en_math_soc_100')) \
        .annotate(student_grade_count=Count(Floor('ko_en_math_soc_100'))) \
        .order_by(Floor('ko_en_math_soc_100'))

    for student_grade in student_grade_freq_qs:
        student_grade_in_list.append(int(student_grade[0]))
        student_grade_in_freq_list.append(student_grade[1])

    # 인문 7등급대 학생 지원대학 현황
    app_univ_name_list = []
    app_univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    app_univ_freq_qs = Student.objects.filter(major_group=2)\
                                     .filter(ko_en_math_soc_100__gte=7)\
                                     .filter(ko_en_math_soc_100__lt=8)\
                                     .values_list('univ_name')\
                                     .annotate(univ_count=Count('univ_name'))\
                                     .order_by('-univ_count')[:25]

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    # 인문 7등급대 학생 지원대학 합격/불합격 인원
    app_univ_pass_freq_list = []
    app_univ_fail_freq_list = []

    for univ in app_univ_name_list:
        app_univ_name = univ_name_qs.get(univ_name=univ)
        app_univ_pass_freq_count = Student.objects.filter(major_group=2) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_soc_100__gte=7) \
            .filter(ko_en_math_soc_100__lt=8) \
            .filter(Q(final_step='합격') | Q(final_step='충원합격')) \
            .count()
        app_univ_fail_freq_count = Student.objects.filter(major_group=2) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_soc_100__gte=7) \
            .filter(ko_en_math_soc_100__lt=8) \
            .filter(final_step='불합격') \
            .count()
        app_univ_pass_freq_list.append(app_univ_pass_freq_count)
        app_univ_fail_freq_list.append(app_univ_fail_freq_count)

        app_univ_pass_freq_list = app_univ_pass_freq_list[:25]
        app_univ_fail_freq_list = app_univ_fail_freq_list[:25]

    context = {
        'student_grade_in_list': student_grade_in_list,
        'student_grade_in_freq_list': student_grade_in_freq_list,

        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,

        'app_univ_pass_freq_list': app_univ_pass_freq_list,
        'app_univ_fail_freq_list': app_univ_fail_freq_list,
    }
    return render(request, template, context)


def app_grade_in_tab_8(request):
    template = "statistic/app_grade_in_tab.html"

    # 등급별 사례수
    student_grade_in_list = []
    student_grade_in_freq_list = []
    student_grade_freq_qs = Student.objects.filter(major_group=2) \
        .values_list(Floor('ko_en_math_soc_100')) \
        .annotate(student_grade_count=Count(Floor('ko_en_math_soc_100'))) \
        .order_by(Floor('ko_en_math_soc_100'))

    for student_grade in student_grade_freq_qs:
        student_grade_in_list.append(int(student_grade[0]))
        student_grade_in_freq_list.append(student_grade[1])

    # 인문 8등급대 학생 지원대학 현황
    app_univ_name_list = []
    app_univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    app_univ_freq_qs = Student.objects.filter(major_group=2)\
                                     .filter(ko_en_math_soc_100__gte=8)\
                                     .filter(ko_en_math_soc_100__lt=9)\
                                     .values_list('univ_name')\
                                     .annotate(univ_count=Count('univ_name'))\
                                     .order_by('-univ_count')[:25]

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    # 인문 8등급대 학생 지원대학 합격/불합격 인원
    app_univ_pass_freq_list = []
    app_univ_fail_freq_list = []

    for univ in app_univ_name_list:
        app_univ_name = univ_name_qs.get(univ_name=univ)
        app_univ_pass_freq_count = Student.objects.filter(major_group=2) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_soc_100__gte=8) \
            .filter(ko_en_math_soc_100__lt=9) \
            .filter(Q(final_step='합격') | Q(final_step='충원합격')) \
            .count()
        app_univ_fail_freq_count = Student.objects.filter(major_group=2) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_soc_100__gte=8) \
            .filter(ko_en_math_soc_100__lt=9) \
            .filter(final_step='불합격') \
            .count()
        app_univ_pass_freq_list.append(app_univ_pass_freq_count)
        app_univ_fail_freq_list.append(app_univ_fail_freq_count)

        app_univ_pass_freq_list = app_univ_pass_freq_list[:25]
        app_univ_fail_freq_list = app_univ_fail_freq_list[:25]

    context = {
        'student_grade_in_list': student_grade_in_list,
        'student_grade_in_freq_list': student_grade_in_freq_list,

        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,

        'app_univ_pass_freq_list': app_univ_pass_freq_list,
        'app_univ_fail_freq_list': app_univ_fail_freq_list,
    }
    return render(request, template, context)


def app_grade_ja(request):
    template = "statistic/app_grade_ja.html"

    # 등급별 사례수
    student_grade_ja_list = []
    student_grade_ja_freq_list = []
    student_grade_freq_qs = Student.objects.filter(major_group=1)\
        .values_list(Floor('ko_en_math_sci_100'))\
        .annotate(student_grade_count=Count(Floor('ko_en_math_sci_100')))\
        .order_by(Floor('ko_en_math_sci_100'))

    for student_grade in student_grade_freq_qs:
        student_grade_ja_list.append(int(student_grade[0]))
        student_grade_ja_freq_list.append(student_grade[1])

    # 자연 1등급대 학생 지원대학 현황
    app_univ_name_list = []
    app_univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    app_univ_freq_qs = Student.objects.filter(major_group=1)\
                                     .filter(ko_en_math_sci_100__lt=2)\
                                     .values_list('univ_name')\
                                     .annotate(univ_count=Count('univ_name'))\
                                     .order_by('-univ_count')[:25]

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    # 자연 1등급대 학생 지원대학 합격/불합격 인원
    app_univ_pass_freq_list = []
    app_univ_fail_freq_list = []

    for univ in app_univ_name_list:
        app_univ_name = univ_name_qs.get(univ_name=univ)
        app_univ_pass_freq_count = Student.objects.filter(major_group=1) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_sci_100__gte=1) \
            .filter(ko_en_math_sci_100__lt=2) \
            .filter(Q(final_step='합격') | Q(final_step='충원합격')) \
            .count()
        app_univ_fail_freq_count = Student.objects.filter(major_group=1) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_sci_100__gte=1) \
            .filter(ko_en_math_sci_100__lt=2) \
            .filter(final_step='불합격') \
            .count()
        app_univ_pass_freq_list.append(app_univ_pass_freq_count)
        app_univ_fail_freq_list.append(app_univ_fail_freq_count)

        app_univ_pass_freq_list = app_univ_pass_freq_list[:25]
        app_univ_fail_freq_list = app_univ_fail_freq_list[:25]

    context = {
        'student_grade_ja_list': student_grade_ja_list,
        'student_grade_ja_freq_list': student_grade_ja_freq_list,

        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,

        'app_univ_pass_freq_list': app_univ_pass_freq_list,
        'app_univ_fail_freq_list': app_univ_fail_freq_list,
    }
    return render(request, template, context)


def app_grade_ja_tab_2(request):
    template = "statistic/app_grade_ja_tab.html"

    # 등급별 사례수
    student_grade_ja_list = []
    student_grade_ja_freq_list = []
    student_grade_freq_qs = Student.objects.filter(major_group=1) \
        .values_list(Floor('ko_en_math_sci_100')) \
        .annotate(student_grade_count=Count(Floor('ko_en_math_sci_100'))) \
        .order_by(Floor('ko_en_math_sci_100'))

    for student_grade in student_grade_freq_qs:
        student_grade_ja_list.append(int(student_grade[0]))
        student_grade_ja_freq_list.append(student_grade[1])

    # 자연 2등급대 학생 지원대학 현황
    app_univ_name_list = []
    app_univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    app_univ_freq_qs = Student.objects.filter(major_group=1)\
                                     .filter(ko_en_math_sci_100__gte=2)\
                                     .filter(ko_en_math_sci_100__lt=3)\
                                     .values_list('univ_name')\
                                     .annotate(univ_count=Count('univ_name'))\
                                     .order_by('-univ_count')[:25]

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    # 자연 2등급대 학생 지원대학 합격/불합격 인원
    app_univ_pass_freq_list = []
    app_univ_fail_freq_list = []

    for univ in app_univ_name_list:
        app_univ_name = univ_name_qs.get(univ_name=univ)
        app_univ_pass_freq_count = Student.objects.filter(major_group=1) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_sci_100__gte=2) \
            .filter(ko_en_math_sci_100__lt=3) \
            .filter(Q(final_step='합격') | Q(final_step='충원합격')) \
            .count()
        app_univ_fail_freq_count = Student.objects.filter(major_group=1) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_sci_100__gte=2) \
            .filter(ko_en_math_sci_100__lt=3) \
            .filter(final_step='불합격') \
            .count()
        app_univ_pass_freq_list.append(app_univ_pass_freq_count)
        app_univ_fail_freq_list.append(app_univ_fail_freq_count)

        app_univ_pass_freq_list = app_univ_pass_freq_list[:25]
        app_univ_fail_freq_list = app_univ_fail_freq_list[:25]

    context = {
        'student_grade_ja_list': student_grade_ja_list,
        'student_grade_ja_freq_list': student_grade_ja_freq_list,

        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,

        'app_univ_pass_freq_list': app_univ_pass_freq_list,
        'app_univ_fail_freq_list': app_univ_fail_freq_list,
    }
    return render(request, template, context)


def app_grade_ja_tab_3(request):
    template = "statistic/app_grade_ja_tab.html"

    # 등급별 사례수
    student_grade_freq_qs = Student.objects.filter(major_group=1) \
        .values_list(Floor('ko_en_math_sci_100')) \
        .annotate(student_grade_count=Count(Floor('ko_en_math_sci_100'))) \
        .order_by(Floor('ko_en_math_sci_100'))
    student_grade_ja_list = []
    student_grade_ja_freq_list = []

    for student_grade in student_grade_freq_qs:
        student_grade_ja_list.append(int(student_grade[0]))
        student_grade_ja_freq_list.append(student_grade[1])

    # 자연 3등급대 학생 지원대학 현황
    app_univ_name_list = []
    app_univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    app_univ_freq_qs = Student.objects.filter(major_group=1)\
                                     .filter(ko_en_math_sci_100__gte=3)\
                                     .filter(ko_en_math_sci_100__lt=4)\
                                     .values_list('univ_name')\
                                     .annotate(univ_count=Count('univ_name'))\
                                     .order_by('-univ_count')[:25]

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    # 자연 3등급대 학생 지원대학 합격/불합격 인원
    app_univ_pass_freq_list = []
    app_univ_fail_freq_list = []

    for univ in app_univ_name_list:
        app_univ_name = univ_name_qs.get(univ_name=univ)
        app_univ_pass_freq_count = Student.objects.filter(major_group=1) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_sci_100__gte=3) \
            .filter(ko_en_math_sci_100__lt=4) \
            .filter(Q(final_step='합격') | Q(final_step='충원합격')) \
            .count()
        app_univ_fail_freq_count = Student.objects.filter(major_group=1) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_sci_100__gte=3) \
            .filter(ko_en_math_sci_100__lt=4) \
            .filter(final_step='불합격') \
            .count()
        app_univ_pass_freq_list.append(app_univ_pass_freq_count)
        app_univ_fail_freq_list.append(app_univ_fail_freq_count)

        app_univ_pass_freq_list = app_univ_pass_freq_list[:25]
        app_univ_fail_freq_list = app_univ_fail_freq_list[:25]

    context = {
        'student_grade_ja_list': student_grade_ja_list,
        'student_grade_ja_freq_list': student_grade_ja_freq_list,

        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,

        'app_univ_pass_freq_list': app_univ_pass_freq_list,
        'app_univ_fail_freq_list': app_univ_fail_freq_list,
    }
    return render(request, template, context)


def app_grade_ja_tab_4(request):
    template = "statistic/app_grade_ja_tab.html"

    # 등급별 사례수
    student_grade_ja_list = []
    student_grade_ja_freq_list = []
    student_grade_freq_qs = Student.objects.filter(major_group=1) \
        .values_list(Floor('ko_en_math_sci_100')) \
        .annotate(student_grade_count=Count(Floor('ko_en_math_sci_100'))) \
        .order_by(Floor('ko_en_math_sci_100'))

    for student_grade in student_grade_freq_qs:
        student_grade_ja_list.append(int(student_grade[0]))
        student_grade_ja_freq_list.append(student_grade[1])

    # 자연 4등급대 학생 지원대학 현황
    app_univ_name_list = []
    app_univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    app_univ_freq_qs = Student.objects.filter(major_group=1)\
                                     .filter(ko_en_math_sci_100__gte=4)\
                                     .filter(ko_en_math_sci_100__lt=5)\
                                     .values_list('univ_name').annotate(univ_count=Count('univ_name'))\
                                     .order_by('-univ_count')[:25]

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    # 자연 4등급대 학생 지원대학 합격/불합격 인원
    app_univ_pass_freq_list = []
    app_univ_fail_freq_list = []

    for univ in app_univ_name_list:
        app_univ_name = univ_name_qs.get(univ_name=univ)
        app_univ_pass_freq_count = Student.objects.filter(major_group=1) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_sci_100__gte=4) \
            .filter(ko_en_math_sci_100__lt=5) \
            .filter(Q(final_step='합격') | Q(final_step='충원합격')) \
            .count()
        app_univ_fail_freq_count = Student.objects.filter(major_group=1) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_sci_100__gte=4) \
            .filter(ko_en_math_sci_100__lt=5) \
            .filter(final_step='불합격') \
            .count()
        app_univ_pass_freq_list.append(app_univ_pass_freq_count)
        app_univ_fail_freq_list.append(app_univ_fail_freq_count)

        app_univ_pass_freq_list = app_univ_pass_freq_list[:25]
        app_univ_fail_freq_list = app_univ_fail_freq_list[:25]

    context = {
        'student_grade_ja_list': student_grade_ja_list,
        'student_grade_ja_freq_list': student_grade_ja_freq_list,

        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,

        'app_univ_pass_freq_list': app_univ_pass_freq_list,
        'app_univ_fail_freq_list': app_univ_fail_freq_list,
    }
    return render(request, template, context)


def app_grade_ja_tab_5(request):
    template = "statistic/app_grade_ja_tab.html"

    # 등급별 사례수
    student_grade_ja_list = []
    student_grade_ja_freq_list = []
    student_grade_freq_qs = Student.objects.filter(major_group=1) \
        .values_list(Floor('ko_en_math_sci_100')) \
        .annotate(student_grade_count=Count(Floor('ko_en_math_sci_100'))) \
        .order_by(Floor('ko_en_math_sci_100'))

    for student_grade in student_grade_freq_qs:
        student_grade_ja_list.append(int(student_grade[0]))
        student_grade_ja_freq_list.append(student_grade[1])

    # 자연 5등급대 학생 지원대학 현황
    app_univ_name_list = []
    app_univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    app_univ_freq_qs = Student.objects.filter(major_group=1)\
                                     .filter(ko_en_math_sci_100__gte=5)\
                                     .filter(ko_en_math_sci_100__lt=6)\
                                     .values_list('univ_name').annotate(univ_count=Count('univ_name'))\
                                     .order_by('-univ_count')[:25]

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    # 자연 5등급대 학생 지원대학 합격/불합격 인원
    app_univ_pass_freq_list = []
    app_univ_fail_freq_list = []

    for univ in app_univ_name_list:
        app_univ_name = univ_name_qs.get(univ_name=univ)
        app_univ_pass_freq_count = Student.objects.filter(major_group=1) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_sci_100__gte=5) \
            .filter(ko_en_math_sci_100__lt=6) \
            .filter(Q(final_step='합격') | Q(final_step='충원합격')) \
            .count()
        app_univ_fail_freq_count = Student.objects.filter(major_group=1) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_sci_100__gte=5) \
            .filter(ko_en_math_sci_100__lt=6) \
            .filter(final_step='불합격') \
            .count()
        app_univ_pass_freq_list.append(app_univ_pass_freq_count)
        app_univ_fail_freq_list.append(app_univ_fail_freq_count)

        app_univ_pass_freq_list = app_univ_pass_freq_list[:25]
        app_univ_fail_freq_list = app_univ_fail_freq_list[:25]

    context = {
        'student_grade_ja_list': student_grade_ja_list,
        'student_grade_ja_freq_list': student_grade_ja_freq_list,

        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,

        'app_univ_pass_freq_list': app_univ_pass_freq_list,
        'app_univ_fail_freq_list': app_univ_fail_freq_list,
    }
    return render(request, template, context)


def app_grade_ja_tab_6(request):
    template = "statistic/app_grade_ja_tab.html"

    # 등급별 사례수
    student_grade_ja_list = []
    student_grade_ja_freq_list = []
    student_grade_freq_qs = Student.objects.filter(major_group=1) \
        .values_list(Floor('ko_en_math_sci_100')) \
        .annotate(student_grade_count=Count(Floor('ko_en_math_sci_100'))) \
        .order_by(Floor('ko_en_math_sci_100'))

    for student_grade in student_grade_freq_qs:
        student_grade_ja_list.append(int(student_grade[0]))
        student_grade_ja_freq_list.append(student_grade[1])

    # 자연 6등급대 학생 지원대학 현황
    app_univ_name_list = []
    app_univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    app_univ_freq_qs = Student.objects.filter(major_group=1)\
                                     .filter(ko_en_math_sci_100__gte=6)\
                                     .filter(ko_en_math_sci_100__lt=7)\
                                     .values_list('univ_name')\
                                     .annotate(univ_count=Count('univ_name'))\
                                     .order_by('-univ_count')[:25]

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    # 자연 6등급대 학생 지원대학 합격/불합격 인원
    app_univ_pass_freq_list = []
    app_univ_fail_freq_list = []

    for univ in app_univ_name_list:
        app_univ_name = univ_name_qs.get(univ_name=univ)
        app_univ_pass_freq_count = Student.objects.filter(major_group=1) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_sci_100__gte=6) \
            .filter(ko_en_math_sci_100__lt=7) \
            .filter(Q(final_step='합격') | Q(final_step='충원합격')) \
            .count()
        app_univ_fail_freq_count = Student.objects.filter(major_group=1) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_sci_100__gte=6) \
            .filter(ko_en_math_sci_100__lt=7) \
            .filter(final_step='불합격') \
            .count()
        app_univ_pass_freq_list.append(app_univ_pass_freq_count)
        app_univ_fail_freq_list.append(app_univ_fail_freq_count)

        app_univ_pass_freq_list = app_univ_pass_freq_list[:25]
        app_univ_fail_freq_list = app_univ_fail_freq_list[:25]

    context = {
        'student_grade_ja_list': student_grade_ja_list,
        'student_grade_ja_freq_list': student_grade_ja_freq_list,

        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,

        'app_univ_pass_freq_list': app_univ_pass_freq_list,
        'app_univ_fail_freq_list': app_univ_fail_freq_list,
    }
    return render(request, template, context)


def app_grade_ja_tab_7(request):
    template = "statistic/app_grade_ja_tab.html"

    # 등급별 사례수
    student_grade_ja_list = []
    student_grade_ja_freq_list = []
    student_grade_freq_qs = Student.objects.filter(major_group=1) \
        .values_list(Floor('ko_en_math_sci_100')) \
        .annotate(student_grade_count=Count(Floor('ko_en_math_sci_100'))) \
        .order_by(Floor('ko_en_math_sci_100'))

    for student_grade in student_grade_freq_qs:
        student_grade_ja_list.append(int(student_grade[0]))
        student_grade_ja_freq_list.append(student_grade[1])

    # 자연 7등급대 학생 지원대학 현황
    app_univ_name_list = []
    app_univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    app_univ_freq_qs = Student.objects.filter(major_group=1)\
                                     .filter(ko_en_math_sci_100__gte=7)\
                                     .filter(ko_en_math_sci_100__lt=8)\
                                     .values_list('univ_name')\
                                     .annotate(univ_count=Count('univ_name'))\
                                     .order_by('-univ_count')[:25]

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    # 자연 7등급대 학생 지원대학 합격/불합격 인원
    app_univ_pass_freq_list = []
    app_univ_fail_freq_list = []

    for univ in app_univ_name_list:
        app_univ_name = univ_name_qs.get(univ_name=univ)
        app_univ_pass_freq_count = Student.objects.filter(major_group=1) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_sci_100__gte=7) \
            .filter(ko_en_math_sci_100__lt=8) \
            .filter(Q(final_step='합격') | Q(final_step='충원합격')) \
            .count()
        app_univ_fail_freq_count = Student.objects.filter(major_group=1) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_sci_100__gte=7) \
            .filter(ko_en_math_sci_100__lt=8) \
            .filter(final_step='불합격') \
            .count()
        app_univ_pass_freq_list.append(app_univ_pass_freq_count)
        app_univ_fail_freq_list.append(app_univ_fail_freq_count)

        app_univ_pass_freq_list = app_univ_pass_freq_list[:25]
        app_univ_fail_freq_list = app_univ_fail_freq_list[:25]

    context = {
        'student_grade_ja_list': student_grade_ja_list,
        'student_grade_ja_freq_list': student_grade_ja_freq_list,

        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,

        'app_univ_pass_freq_list': app_univ_pass_freq_list,
        'app_univ_fail_freq_list': app_univ_fail_freq_list,
    }
    return render(request, template, context)


def app_grade_ja_tab_8(request):
    template = "statistic/app_grade_ja_tab.html"

    # 등급별 사례수
    student_grade_ja_list = []
    student_grade_ja_freq_list = []
    student_grade_freq_qs = Student.objects.filter(major_group=1) \
        .values_list(Floor('ko_en_math_sci_100')) \
        .annotate(student_grade_count=Count(Floor('ko_en_math_sci_100'))) \
        .order_by(Floor('ko_en_math_sci_100'))

    for student_grade in student_grade_freq_qs:
        student_grade_ja_list.append(int(student_grade[0]))
        student_grade_ja_freq_list.append(student_grade[1])

    # 자연 8등급대 학생 지원대학 현황
    app_univ_name_list = []
    app_univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    app_univ_freq_qs = Student.objects.filter(major_group=1)\
                                     .filter(ko_en_math_sci_100__gte=8)\
                                     .filter(ko_en_math_sci_100__lt=9)\
                                     .values_list('univ_name')\
                                     .annotate(univ_count=Count('univ_name'))\
                                     .order_by('-univ_count')[:25]

    for univ in app_univ_freq_qs:
        app_univ_name = univ_name_qs.get(pk=univ[0])
        app_univ_name_list.append(app_univ_name.univ_name)
        app_univ_freq_list.append(univ[1])

    # 자연 8등급대 학생 지원대학 합격/불합격 인원
    app_univ_pass_freq_list = []
    app_univ_fail_freq_list = []

    for univ in app_univ_name_list:
        app_univ_name = univ_name_qs.get(univ_name=univ)
        app_univ_pass_freq_count = Student.objects.filter(major_group=1) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_sci_100__gte=8) \
            .filter(ko_en_math_sci_100__lt=9) \
            .filter(Q(final_step='합격') | Q(final_step='충원합격')) \
            .count()
        app_univ_fail_freq_count = Student.objects.filter(major_group=1) \
            .filter(univ_name=app_univ_name.id) \
            .filter(ko_en_math_sci_100__gte=8) \
            .filter(ko_en_math_sci_100__lt=9) \
            .filter(final_step='불합격') \
            .count()
        app_univ_pass_freq_list.append(app_univ_pass_freq_count)
        app_univ_fail_freq_list.append(app_univ_fail_freq_count)

        app_univ_pass_freq_list = app_univ_pass_freq_list[:25]
        app_univ_fail_freq_list = app_univ_fail_freq_list[:25]

    context = {
        'student_grade_ja_list': student_grade_ja_list,
        'student_grade_ja_freq_list': student_grade_ja_freq_list,

        'app_univ_name_list': app_univ_name_list,
        'app_univ_freq_list': app_univ_freq_list,

        'app_univ_pass_freq_list': app_univ_pass_freq_list,
        'app_univ_fail_freq_list': app_univ_fail_freq_list,
    }
    return render(request, template, context)
from django.shortcuts import render
from analysis.models import *
from django.db.models import Count


def app_region(request):
    template = "statistic/app_region.html"

    # 지역별 사례수
    chart0_student_region_freq_qs = Student.objects.values_list('student_region') \
                              .annotate(student_region_count=Count('student_region')) \
                              .order_by('-student_region_count')
    chart0_student_region_list = []
    chart0_student_region_freq_list = []

    for chart0_student_region in chart0_student_region_freq_qs:
        chart0_student_region_list.append(chart0_student_region[0])
        chart0_student_region_freq_list.append(chart0_student_region[1])

    # 충청도지역 학생 지원대학 현황
    univ_name_qs = UnivName.objects.all()

    chart1_sum = Student.objects.all().count()
    chart1_univ_freq_qs = Student.objects.values_list('univ_name')\
                              .annotate(univ_count=Count('univ_name'))\
                              .order_by('-univ_count')[:10]
    chart1_univ_name_list = []
    chart1_univ_freq_list = []

    for univ in chart1_univ_freq_qs:
        chart1_univ_name = univ_name_qs.get(pk=univ[0])
        chart1_univ_name_list.append(chart1_univ_name.univ_name)
        chart1_univ_freq_list.append(univ[1])

    context = {
        'chart0_student_region_list': chart0_student_region_list,
        'chart0_student_region_freq_list': chart0_student_region_freq_list,
        'chart1_sum': chart1_sum,
        'chart1_univ_name_list': chart1_univ_name_list,
        'chart1_univ_freq_list': chart1_univ_freq_list,

    }
    return render(request, template, context)

def app_tap_region_dj(request):
    template = "statistic/app_region_tab_dj.html"

    univ_name_qs = UnivName.objects.all()

    # 지역별 사례수
    chart0_student_region_freq_qs = Student.objects.values_list('student_region') \
        .annotate(student_region_count=Count('student_region')) \
        .order_by('-student_region_count')
    chart0_student_region_list = []
    chart0_student_region_freq_list = []

    for chart0_student_region in chart0_student_region_freq_qs:
        chart0_student_region_list.append(chart0_student_region[0])
        chart0_student_region_freq_list.append(chart0_student_region[1])

    # 대전지역 학생 지원대학 현황
    application_dj_sum = Student.objects.filter(student_region='대전').count()
    application_univ_freq_dj_qs = Student.objects.filter(student_region='대전').values_list('univ_name').annotate(
        univ_count=Count('univ_name')).order_by('-univ_count')[:10]
    application_univ_name_dj_list = []
    application_univ_freq_dj_list = []

    for univ in application_univ_freq_dj_qs:
        application_univ_name_dj = univ_name_qs.get(pk=univ[0])
        application_univ_name_dj_list.append(application_univ_name_dj.univ_name)
        application_univ_freq_dj_list.append(univ[1])

    context = {
        'chart0_student_region_list': chart0_student_region_list,
        'chart0_student_region_freq_list': chart0_student_region_freq_list,

        'application_dj_sum': application_dj_sum,
        'application_univ_name_dj_list': application_univ_name_dj_list,
        'application_univ_freq_dj_list': application_univ_freq_dj_list,
    }
    return render(request, template, context)


def app_tap_region_sj(request):
    template = "statistic/app_region_tab_sj.html"

    # 지역별 사례수
    chart0_student_region_freq_qs = Student.objects.values_list('student_region') \
        .annotate(student_region_count=Count('student_region')) \
        .order_by('-student_region_count')
    chart0_student_region_list = []
    chart0_student_region_freq_list = []

    for chart0_student_region in chart0_student_region_freq_qs:
        chart0_student_region_list.append(chart0_student_region[0])
        chart0_student_region_freq_list.append(chart0_student_region[1])

    univ_name_qs = UnivName.objects.all()

    # 세종지역 학생 지원대학 현황
    application_sj_sum = Student.objects.filter(student_region='세종').count()
    application_univ_freq_sj_qs = Student.objects.filter(student_region='세종').values_list('univ_name').annotate(
        univ_count=Count('univ_name')).order_by('-univ_count')[:10]
    application_univ_name_sj_list = []
    application_univ_freq_sj_list = []

    for univ in application_univ_freq_sj_qs:
        application_univ_name_sj = univ_name_qs.get(pk=univ[0])
        application_univ_name_sj_list.append(application_univ_name_sj.univ_name)
        application_univ_freq_sj_list.append(univ[1])

    context = {
        'chart0_student_region_list': chart0_student_region_list,
        'chart0_student_region_freq_list': chart0_student_region_freq_list,

        'application_sj_sum': application_sj_sum,
        'application_univ_name_sj_list': application_univ_name_sj_list,
        'application_univ_freq_sj_list': application_univ_freq_sj_list,
    }
    return render(request, template, context)


def app_tap_region_cn(request):
    template = "statistic/app_region_tab_cn.html"

    # 지역별 사례수
    chart0_student_region_freq_qs = Student.objects.values_list('student_region') \
        .annotate(student_region_count=Count('student_region')) \
        .order_by('-student_region_count')
    chart0_student_region_list = []
    chart0_student_region_freq_list = []

    for chart0_student_region in chart0_student_region_freq_qs:
        chart0_student_region_list.append(chart0_student_region[0])
        chart0_student_region_freq_list.append(chart0_student_region[1])

    univ_name_qs = UnivName.objects.all()

    # 충남지역 학생 지원대학 현황
    application_cn_sum = Student.objects.filter(student_region='충남').count()
    application_univ_freq_cn_qs = Student.objects.filter(student_region='충남').values_list('univ_name').annotate(
        univ_count=Count('univ_name')).order_by('-univ_count')[:10]
    application_univ_name_cn_list = []
    application_univ_freq_cn_list = []

    for univ in application_univ_freq_cn_qs:
        application_univ_name_cn = univ_name_qs.get(pk=univ[0])
        application_univ_name_cn_list.append(application_univ_name_cn.univ_name)
        application_univ_freq_cn_list.append(univ[1])

    context = {
        'chart0_student_region_list': chart0_student_region_list,
        'chart0_student_region_freq_list': chart0_student_region_freq_list,

        'application_cn_sum': application_cn_sum,
        'application_univ_name_cn_list': application_univ_name_cn_list,
        'application_univ_freq_cn_list': application_univ_freq_cn_list,
    }
    return render(request, template, context)


def app_tap_region_cb(request):
    template = "statistic/app_region_tab_cb.html"

    # 지역별 사례수
    chart0_student_region_freq_qs = Student.objects.values_list('student_region') \
        .annotate(student_region_count=Count('student_region')) \
        .order_by('-student_region_count')
    chart0_student_region_list = []
    chart0_student_region_freq_list = []

    for chart0_student_region in chart0_student_region_freq_qs:
        chart0_student_region_list.append(chart0_student_region[0])
        chart0_student_region_freq_list.append(chart0_student_region[1])

    univ_name_qs = UnivName.objects.all()

    # 충북지역 학생 지원대학 현황
    application_cb_sum = Student.objects.filter(student_region='충북').count()
    application_univ_freq_cb_qs = Student.objects.filter(student_region='충북').values_list('univ_name').annotate(
        univ_count=Count('univ_name')).order_by('-univ_count')[:10]
    application_univ_name_cb_list = []
    application_univ_freq_cb_list = []

    for univ in application_univ_freq_cb_qs:
        application_univ_name_cb = univ_name_qs.get(pk=univ[0])
        application_univ_name_cb_list.append(application_univ_name_cb.univ_name)
        application_univ_freq_cb_list.append(univ[1])

    context = {
        'chart0_student_region_list': chart0_student_region_list,
        'chart0_student_region_freq_list': chart0_student_region_freq_list,

        'application_cb_sum': application_cb_sum,
        'application_univ_name_cb_list': application_univ_name_cb_list,
        'application_univ_freq_cb_list': application_univ_freq_cb_list,
    }
    return render(request, template, context)
from django.shortcuts import render
from analysis.models import *
from django.db.models import Count


def statistic1(request):
    template = "statistic/statistic1.html"

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


    chart2_sum = Student.objects.filter(student_region='충남').count()
    chart2_univ_freq_qs = Student.objects.filter(student_region='충남')\
                              .values_list('univ_name')\
                              .annotate(univ_count=Count('univ_name'))\
                              .order_by('-univ_count')[:10]
    chart2_univ_name_list = []
    chart2_univ_freq_list = []

    for univ in chart2_univ_freq_qs:
        chart2_univ_name = univ_name_qs.get(pk=univ[0])
        chart2_univ_name_list.append(chart2_univ_name.univ_name)
        chart2_univ_freq_list.append(univ[1])

    context = {
        'chart1_sum': chart1_sum,
        'chart1_univ_name_list': chart1_univ_name_list,
        'chart1_univ_freq_list': chart1_univ_freq_list,
        'chart2_sum': chart2_sum,
        'chart2_univ_name_list': chart2_univ_name_list,
        'chart2_univ_freq_list': chart2_univ_freq_list,
    }
    return render(request, template, context)

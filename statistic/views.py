from django.shortcuts import render
from analysis.models import *
from django.db.models import Count


def statistic1(request):
    template = "statistic/statistic1.html"

    univ_name_qs = UnivName.objects.all()
    student_sum = Student.objects.all().count()
    univ_freq_qs = Student.objects.values_list('univ_name')\
                       .annotate(univ_count=Count('univ_name'))\
                       .order_by('-univ_count')[:10]
    univ_name_list = []
    univ_freq_list = []

    for univ in univ_freq_qs:
        univ_name = univ_name_qs.get(pk=univ[0])
        univ_name_list.append(univ_name.univ_name)
        univ_freq_list.append(univ[1])

    context = {
        'student_sum': student_sum,
        'univ_name': univ_name_list,
        'univ_freq': univ_freq_list,
    }
    return render(request, template, context)

from django.shortcuts import render
from analysis.models import *


def statistic1(request):
    template = "statistic/statistic1.html"

    student_sum = Student.objects.all().count();
    student_qs = Student.objects.filter();

    context = {
        'student_sum': student_sum,
    }
    return render(request, template, context)

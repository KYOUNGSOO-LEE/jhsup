from django.shortcuts import render
from .models import *
from .forms import AdvancedForm


def grade(request):
    template = "analysis/grade_interval_search.html"

    major_group_qs = MajorGroup.objects.all().order_by('major_group')
    univ_region_qs = UnivRegion.objects.all().order_by('univ_region')

    context = {
        'major_group_item': major_group_qs,
        'univ_region_item': univ_region_qs
    }
    return render(request, template, context)


def grade_search(request):
    template = "analysis/grade_interval_search.html"

    major_group_qs = MajorGroup.objects.all().order_by('major_group')
    univ_region_qs = UnivRegion.objects.all().order_by('univ_region')
    student_qs = Student.objects.all()
    final_step = ['합격', '충원합격', '불합격']

    major_group_query = request.GET.get('major_group')
    univ_region_query = request.GET.get('univ_region')
    ko_en_math_soc_or_sci_100_min_query = request.GET.get('ko_en_math_soc_or_sci_100_min')
    ko_en_math_soc_or_sci_100_max_query = request.GET.get('ko_en_math_soc_or_sci_100_max')

    current_major_group_str = str(major_group_qs.get(pk=major_group_query))

    if major_group_query != '' and major_group_query is not None:
        student_qs = student_qs.filter(major_group=major_group_query)

    if univ_region_query != '' and univ_region_query is not None:
        if univ_region_query == '지역 전체':
            student_qs = student_qs
        else:
            student_qs = student_qs.filter(univ_region=univ_region_query)

    if ko_en_math_soc_or_sci_100_min_query != '' and ko_en_math_soc_or_sci_100_min_query is not None:
        if current_major_group_str == '자연':
            student_qs = student_qs.filter(ko_en_math_sci_100__gte=ko_en_math_soc_or_sci_100_min_query)
        elif current_major_group_str == '공통':
            student_qs = student_qs.filter(ko_en_math_soc_sci_100__gte=ko_en_math_soc_or_sci_100_min_query)
        else:
            student_qs = student_qs.filter(ko_en_math_soc_100__gte=ko_en_math_soc_or_sci_100_min_query)

    if ko_en_math_soc_or_sci_100_max_query != '' and ko_en_math_soc_or_sci_100_max_query is not None:
        if current_major_group_str == '자연':
            student_qs = student_qs.filter(ko_en_math_sci_100__lte=ko_en_math_soc_or_sci_100_max_query)
        elif current_major_group_str == '공통':
            student_qs = student_qs.filter(ko_en_math_soc_sci_100__lte=ko_en_math_soc_or_sci_100_max_query)
        else:
            student_qs = student_qs.filter(ko_en_math_soc_100__lte=ko_en_math_soc_or_sci_100_max_query)

    if current_major_group_str == '자연':
        student_qs = student_qs.order_by('-final_step', 'ko_en_math_sci_100')
    elif current_major_group_str == '공통':
        student_qs = student_qs.order_by('-final_step', 'ko_en_math_soc_sci_100')
    else:
        student_qs = student_qs.order_by('-final_step', 'ko_en_math_soc_100')

    context = {
        'queryset': student_qs,
        'major_group_item': major_group_qs,
        'univ_region_item': univ_region_qs,
        'current_major_group': int(major_group_query),
        'current_univ_region': int(univ_region_query),
        'current_major_group_str': current_major_group_str,
        'current_ko_en_math_soc_or_sci_100_min': ko_en_math_soc_or_sci_100_min_query,
        'current_ko_en_math_soc_or_sci_100_max': ko_en_math_soc_or_sci_100_max_query,
        'final_step': final_step
    }
    return render(request, template, context)


def major(request):
    template = "analysis/univ_major_search.html"

    major_group_qs = MajorGroup.objects.all().order_by('major_group')

    context = {
        'major_group_item': major_group_qs
    }
    return render(request, template, context)


def major_search(request):
    template = "analysis/univ_major_search.html"

    major_group_qs = MajorGroup.objects.all().order_by('major_group')
    univ_major_qs = UnivMajor.objects.all()
    student_qs = Student.objects.all()
    final_step = ['합격', '충원합격', '불합격']

    major_group_query = request.GET.get('major_group')
    univ_major_query = request.GET.get('univ_major')
    ko_en_math_soc_or_sci_100_min_query = request.GET.get('ko_en_math_soc_or_sci_100_min')
    ko_en_math_soc_or_sci_100_max_query = request.GET.get('ko_en_math_soc_or_sci_100_max')

    current_major_group_str = str(major_group_qs.get(pk=major_group_query))

    if major_group_query != '' and major_group_query is not None:
        student_qs = student_qs.filter(major_group=major_group_query)

    if univ_major_query != '' and univ_major_query is not None:
        univ_major_qs = univ_major_qs.filter(univ_major__icontains=univ_major_query)

        union_qs = Student.objects.none()
        for univ_major in univ_major_qs:
            union_qs = union_qs | student_qs.filter(univ_major=univ_major.id)
        student_qs = union_qs

    if ko_en_math_soc_or_sci_100_min_query != '' and ko_en_math_soc_or_sci_100_min_query is not None:
        if current_major_group_str == '자연':
            student_qs = student_qs.filter(ko_en_math_sci_100__gte=ko_en_math_soc_or_sci_100_min_query)
        elif current_major_group_str == '공통':
            student_qs = student_qs.filter(ko_en_math_soc_sci_100__gte=ko_en_math_soc_or_sci_100_min_query)
        else:
            student_qs = student_qs.filter(ko_en_math_soc_100__gte=ko_en_math_soc_or_sci_100_min_query)

    if ko_en_math_soc_or_sci_100_max_query != '' and ko_en_math_soc_or_sci_100_max_query is not None:
        if current_major_group_str == '자연':
            student_qs = student_qs.filter(ko_en_math_sci_100__lte=ko_en_math_soc_or_sci_100_max_query)
        elif current_major_group_str == '공통':
            student_qs = student_qs.filter(ko_en_math_soc_sci_100__lte=ko_en_math_soc_or_sci_100_max_query)
        else:
            student_qs = student_qs.filter(ko_en_math_soc_100__lte=ko_en_math_soc_or_sci_100_max_query)

    if current_major_group_str == '자연':
        student_qs = student_qs.order_by('-final_step', 'ko_en_math_sci_100')
    elif current_major_group_str == '공통':
        student_qs = student_qs.order_by('-final_step', 'ko_en_math_soc_sci_100')
    else:
        student_qs = student_qs.order_by('-final_step', 'ko_en_math_soc_100')

    context = {
        'queryset': student_qs,
        'major_group_item': major_group_qs,
        'current_major_group': int(major_group_query),
        'current_univ_major': univ_major_query,
        'current_major_group_str': current_major_group_str,
        'current_ko_en_math_soc_or_sci_100_min': ko_en_math_soc_or_sci_100_min_query,
        'current_ko_en_math_soc_or_sci_100_max': ko_en_math_soc_or_sci_100_max_query,
        'final_step': final_step
    }
    return render(request, template, context)


def advanced(request):
    template = "analysis/advanced_search.html"

    form = AdvancedForm('', '', '')

    context = {
        'form': form,
    }
    return render(request, template, context)


def advanced_search(request):
    template = "analysis/advanced_search.html"

    major_group_qs = MajorGroup.objects.all().order_by('major_group')
    final_step = ['합격', '충원합격', '불합격']

    qs = Student.objects.all()
    major_group_query = request.GET.get('major_group')
    univ_region_query = request.GET.get('univ_region')
    univ_name_query = request.GET.get('univ_name')
    univ_major_query = request.GET.get('univ_major')
    admission1_query = request.GET.get('admission1')

    current_major_group_str = str(major_group_qs.get(pk=major_group_query))

    if major_group_query != '' and major_group_query is not None:
        qs = qs.filter(major_group=major_group_query)

    if univ_region_query != '' and univ_region_query is not None:
        qs = qs.filter(univ_region=univ_region_query)

    if univ_name_query != '' and univ_name_query is not None:
        qs = qs.filter(univ_name=univ_name_query)

    if univ_major_query != '' and univ_major_query is not None:
        qs = qs.filter(univ_major=univ_major_query)

    if admission1_query != '' and admission1_query is not None:
        qs = qs.filter(admission1=admission1_query)

    if current_major_group_str == '자연':
        qs = qs.order_by('-final_step', 'ko_en_math_sci_100')
    elif current_major_group_str == '공통':
        qs = qs.order_by('-final_step', 'ko_en_math_soc_sci_100')
    else:
        qs = qs.order_by('-final_step', 'ko_en_math_soc_100')

    form = AdvancedForm(univ_region_query,
                        univ_name_query,
                        univ_major_query,
                        initial={'major_group': major_group_query,
                                 'univ_region': univ_region_query,
                                 'univ_name': univ_name_query,
                                 'univ_major': univ_major_query,
                                 'admission1': admission1_query,
                        }
    )

    context = {
        'form': form,
        'queryset': qs,
        'final_step': final_step,
        'current_major_group': int(major_group_query),
        'current_major_group_str': current_major_group_str,
    }
    return render(request, template, context)


def university(request):
    template = "analysis/univ_name_search.html"

    major_group_qs = MajorGroup.objects.all().order_by('major_group')

    context = {
        'major_group_item': major_group_qs
    }
    return render(request, template, context)


def university_search(request):
    template = "analysis/univ_name_search.html"

    major_group_qs = MajorGroup.objects.all().order_by('major_group')
    univ_name_qs = UnivName.objects.all()
    student_qs = Student.objects.all()
    final_step = ['합격', '충원합격', '불합격']

    major_group_query = request.GET.get('major_group')
    univ_name_query = request.GET.get('univ_name')
    ko_en_math_soc_or_sci_100_min_query = request.GET.get('ko_en_math_soc_or_sci_100_min')
    ko_en_math_soc_or_sci_100_max_query = request.GET.get('ko_en_math_soc_or_sci_100_max')

    current_major_group_str = str(major_group_qs.get(pk=major_group_query))

    if major_group_query != '' and major_group_query is not None:
        student_qs = student_qs.filter(major_group=major_group_query)

    if univ_name_query != '' and univ_name_query is not None:
        univ_name_qs = univ_name_qs.filter(univ_name__icontains=univ_name_query)

        union_qs = Student.objects.none()
        for univ_name in univ_name_qs:
            union_qs = union_qs | student_qs.filter(univ_name=univ_name.id)
        student_qs = union_qs

    if ko_en_math_soc_or_sci_100_min_query != '' and ko_en_math_soc_or_sci_100_min_query is not None:
        if current_major_group_str == '자연':
            student_qs = student_qs.filter(ko_en_math_sci_100__gte=ko_en_math_soc_or_sci_100_min_query)
        elif current_major_group_str == '공통':
            student_qs = student_qs.filter(ko_en_math_soc_sci_100__gte=ko_en_math_soc_or_sci_100_min_query)
        else:
            student_qs = student_qs.filter(ko_en_math_soc_100__gte=ko_en_math_soc_or_sci_100_min_query)

    if ko_en_math_soc_or_sci_100_max_query != '' and ko_en_math_soc_or_sci_100_max_query is not None:
        if current_major_group_str == '자연':
            student_qs = student_qs.filter(ko_en_math_sci_100__lte=ko_en_math_soc_or_sci_100_max_query)
        elif current_major_group_str == '공통':
            student_qs = student_qs.filter(ko_en_math_soc_sci_100__lte=ko_en_math_soc_or_sci_100_max_query)
        else:
            student_qs = student_qs.filter(ko_en_math_soc_100__lte=ko_en_math_soc_or_sci_100_max_query)

    if current_major_group_str == '자연':
        student_qs = student_qs.order_by('-final_step', 'ko_en_math_sci_100')
    elif current_major_group_str == '공통':
        student_qs = student_qs.order_by('-final_step', 'ko_en_math_soc_sci_100')
    else:
        student_qs = student_qs.order_by('-final_step', 'ko_en_math_soc_100')

    context = {
        'queryset': student_qs,
        'major_group_item': major_group_qs,
        'current_major_group': int(major_group_query),
        'current_univ_name': univ_name_query,
        'current_major_group_str': current_major_group_str,
        'current_ko_en_math_soc_or_sci_100_min': ko_en_math_soc_or_sci_100_min_query,
        'current_ko_en_math_soc_or_sci_100_max': ko_en_math_soc_or_sci_100_max_query,
        'final_step': final_step
    }
    return render(request, template, context)
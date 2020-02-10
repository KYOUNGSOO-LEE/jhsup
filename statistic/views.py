from django.shortcuts import render
from analysis.models import *
from django.db.models import Count, Avg
from django.db.models.functions import Floor
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def student_region(request):
    template = "statistic/student_region.html"

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

    # 출신지역 비율(pie chart, table chart)
    student_region_pie = []
    student_region_table = []
    n = sum(student_region_freq_list)
    for i in range(0,len(student_region_list)):
        student_region_pie.append([
            student_region_list[i],
            student_region_freq_list[i]
        ])
        student_region_table.append([
            student_region_list[i],
            student_region_freq_list[i],
            round((student_region_freq_list[i]/n) * 100, 1)
        ])
    student_region_table.append([
        '합',
        sum(student_region_freq_list),
        (sum(student_region_freq_list) / n) * 100
    ])

    # 출신지역기준 지원대학
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

    # 출신지역기준 지원대학 합격/불합격(bar chart)
    univ_pass_freq_list = []
    univ_supplement_freq_list = []
    univ_fail_freq_list = []
    univ_psf_bar = [['대학명', '합격', {'role': 'style'} , '충원합격', {'role': 'style'}, '불합격', {'role': 'style'}]]

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

    for i in range(0, len(univ_name_list)):
        univ_psf_bar.append([
            univ_name_list[i],
            univ_pass_freq_list[i],
            'stroke-color: #000000; stroke-width: 1; opacity: 0.5',
            univ_supplement_freq_list[i],
            'stroke-color: #000000; stroke-width: 1; opacity: 0.5',
            univ_fail_freq_list[i],
            'stroke-color: #000000; stroke-width: 1; opacity: 0.5',
        ])

    context = {
        'entrance_year_item': entrance_year_qs,
        'current_entrance_year': entrance_year_query,
        'current_region': student_region_query,

        'student_region_pie': student_region_pie,
        'student_region_table': student_region_table,
        'univ_psf_bar': univ_psf_bar
    }
    return render(request, template, context)


@login_required(login_url="login")
def major_group(request):
    template = "statistic/major_group.html"

    entrance_year_qs = Student.objects.values('entrance_year').order_by('entrance_year').distinct()
    major_group_qs = MajorGroup.objects.order_by('major_group').distinct()

    context = {
        'entrance_year_item': entrance_year_qs,
        'major_group_item': major_group_qs,
    }
    return render(request, template, context)


@login_required(login_url="login")
def major_group_result(request):
    template = "statistic/major_group_result.html"

    entrance_year_qs = Student.objects.values('entrance_year').order_by('entrance_year').distinct()
    major_group_qs = MajorGroup.objects.order_by('major_group').distinct()
    univ_region_qs = UnivRegion.objects.order_by('univ_region').distinct()
    admission1_qs = Admission1.objects.values('admission1').order_by('admission1').distinct()

    entrance_year_query = request.GET.get('entrance_year')
    major_group_query = request.GET.get('major_group')

    # 계열기준 전형비율(pie chart)
    admission1_list = []
    admission1_freq_list = []

    for admission1 in admission1_qs:
        admission1 = list(admission1.values())[0]
        admission1_freq = Student.objects \
            .filter(entrance_year=entrance_year_query) \
            .filter(major_group=major_group_query) \
            .filter(admission1__admission1__contains=admission1) \
            .count()
        admission1_list.append(admission1)
        admission1_freq_list.append(admission1_freq)

    admission1_pie = []
    for i in range(0, len(admission1_list)):
        admission1_pie.append([admission1_list[i], admission1_freq_list[i]])

    # 계열기준 등급분포(column chart)
    grade_list = []
    grade_freq_list = []
    grade_column1 = [['등급', '사례수', {'role': 'style'}]]

    if str(MajorGroup.objects.get(pk=major_group_query)) == '자연':
        grade_freq_qs = Student.objects \
            .filter(entrance_year=entrance_year_query) \
            .filter(major_group=major_group_query) \
            .values_list(Floor('ko_en_math_sci_100')) \
            .annotate(student_grade_count=Count(Floor('ko_en_math_sci_100')))
    elif str(MajorGroup.objects.get(pk=major_group_query)) == '공통':
        grade_freq_qs = Student.objects \
            .filter(entrance_year=entrance_year_query) \
            .filter(major_group=major_group_query) \
            .values_list(Floor('ko_en_math_soc_sci_100')) \
            .annotate(student_grade_count=Count(Floor('ko_en_math_soc_sci_100')))
    else:
        grade_freq_qs = Student.objects \
            .filter(entrance_year=entrance_year_query) \
            .filter(major_group=major_group_query) \
            .values_list(Floor('ko_en_math_soc_100')) \
            .annotate(student_grade_count=Count(Floor('ko_en_math_soc_100')))

    for grade in grade_freq_qs:
        grade_list.append(int(grade[0]))
        grade_freq_list.append(grade[1])

    for i in range(0, len(grade_list)):
        grade_column1.append([
            grade_list[i],
            grade_freq_list[i],
            'stroke-color: #000000; stroke-width: 2; opacity: 0.8',
        ])

    # 계열기준 등급분포(table chart)
    grade_column1_table = []
    admission1_list = []
    sum_list = ['합', 0, 0, 0, 0, 0]

    for i in range(1, 9):
        grade_column1_table.append([str(i), 0, 0, 0, 0, 0])

    for idx, admission1 in enumerate(admission1_qs):
        if str(MajorGroup.objects.get(pk=major_group_query)) == '자연':
            grade_freq_qs = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(major_group=major_group_query) \
                .filter(admission1__admission1__contains=admission1['admission1']) \
                .values_list(Floor('ko_en_math_sci_100')) \
                .annotate(student_grade_count=Count(Floor('ko_en_math_sci_100')))
        elif str(MajorGroup.objects.get(pk=major_group_query)) == '공통':
            grade_freq_qs = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(major_group=major_group_query) \
                .filter(admission1__admission1__contains=admission1['admission1']) \
                .values_list(Floor('ko_en_math_soc_sci_100')) \
                .annotate(student_grade_count=Count(Floor('ko_en_math_soc_sci_100')))
        else:
            grade_freq_qs = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(major_group=major_group_query) \
                .filter(admission1__admission1__contains=admission1['admission1']) \
                .values_list(Floor('ko_en_math_soc_100')) \
                .annotate(student_grade_count=Count(Floor('ko_en_math_soc_100')))

        for data in grade_freq_qs:
            grade_column1_table[int(data[0] - 1)][idx + 1] = data[1]

        admission1_list.append(admission1['admission1'])

    for row in grade_column1_table:
        row[5] = sum(row[1:5])
        for i in range(1, 6):
            sum_list[i] += row[i]
    grade_column1_table.append(sum_list)

    # 계열기준 대학소재 비율(pie chart)
    univ_region_list = []
    univ_region_freq_list = []

    for univ_region in univ_region_qs:
        univ_region = univ_region.univ_region
        univ_region_freq = Student.objects \
            .filter(entrance_year=entrance_year_query) \
            .filter(major_group=major_group_query) \
            .filter(univ_region__univ_region__contains=univ_region) \
            .count()
        univ_region_list.append(univ_region)
        univ_region_freq_list.append(univ_region_freq)

    univ_region_pie = []
    for i in range(0, len(univ_region_list)):
        univ_region_pie.append([univ_region_list[i], univ_region_freq_list[i]])
    univ_region_pie.sort(key=lambda x: x[1])

    context = {
        'entrance_year_item': entrance_year_qs,
        'major_group_item': major_group_qs,

        'current_entrance_year': entrance_year_query,
        'current_major_group': int(major_group_query),
        'current_major_group_str': str(MajorGroup.objects.get(pk=major_group_query)),

        'admission1_list': admission1_list,

        'admission1_pie': admission1_pie,
        'grade_column1': grade_column1,
        'grade_column1_table': grade_column1_table,
        'univ_region_pie': univ_region_pie,
    }
    return render(request, template, context)


@login_required(login_url="login")
def admission1(request):
    template = "statistic/admission1.html"

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
def admission1_result(request):
    template = "statistic/admission1_result.html"

    entrance_year_qs = Student.objects.values('entrance_year').order_by('entrance_year').distinct()
    major_group_qs = MajorGroup.objects.order_by('major_group').distinct()
    admission1_qs = Admission1.objects.values('admission1').order_by('admission1').distinct()

    entrance_year_query = request.GET.get('entrance_year')
    major_group_query = request.GET.get('major_group')
    admission1_query = request.GET.get('admission1')
    gte_query = request.GET.get('gte')
    lt_query = request.GET.get('lt')

    #계열, 전형기준 등급분포(column chart)
    grade_list = []
    grade_freq_list = []
    grade_column2 = [['등급', '사례수', {'role': 'style'}]]

    if str(MajorGroup.objects.get(pk=major_group_query)) == '자연':
        grade_freq_qs = Student.objects\
            .filter(entrance_year=entrance_year_query) \
            .filter(major_group=major_group_query) \
            .filter(admission1__admission1__contains=admission1_query)\
            .values_list(Floor('ko_en_math_sci_100'))\
            .annotate(student_grade_count=Count(Floor('ko_en_math_sci_100')))
    elif str(MajorGroup.objects.get(pk=major_group_query)) == '공통':
        grade_freq_qs = Student.objects \
            .filter(entrance_year=entrance_year_query) \
            .filter(major_group=major_group_query) \
            .filter(admission1__admission1__contains=admission1_query) \
            .values_list(Floor('ko_en_math_soc_sci_100')) \
            .annotate(student_grade_count=Count(Floor('ko_en_math_soc_sci_100')))
    else:
        grade_freq_qs = Student.objects \
            .filter(entrance_year=entrance_year_query) \
            .filter(major_group=major_group_query) \
            .filter(admission1__admission1__contains=admission1_query) \
            .values_list(Floor('ko_en_math_soc_100')) \
            .annotate(student_grade_count=Count(Floor('ko_en_math_soc_100')))

    for grade in grade_freq_qs:
        grade_list.append(int(grade[0]))
        grade_freq_list.append(grade[1])

    for i in range(0, len(grade_list)):
        if int(gte_query) == i + 1:
            grade_column2.append([
                grade_list[i],
                grade_freq_list[i],
                'color: #FFBB00; stroke-color: #000000; stroke-width: 2; opacity: 0.8',
            ])
        else:
            grade_column2.append([
                grade_list[i],
                grade_freq_list[i],
                'color: #3162C7; stroke-color: #000000; stroke-width: 2; opacity: 0.8',
            ])

    #계열, 전형기준 등급분포(table chart)1
    grade_column1_table = []
    admission1_list = []
    sum_list = ['합', 0, 0, 0, 0, 0]

    for i in range(1, 9):
        grade_column1_table.append([str(i), 0, 0, 0, 0, 0])

    for idx, admission1 in enumerate(admission1_qs):
        if str(MajorGroup.objects.get(pk=major_group_query)) == '자연':
            grade_freq_qs = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(major_group=major_group_query) \
                .filter(admission1__admission1__contains=admission1['admission1']) \
                .values_list(Floor('ko_en_math_sci_100')) \
                .annotate(student_grade_count=Count(Floor('ko_en_math_sci_100')))
        elif str(MajorGroup.objects.get(pk=major_group_query)) == '공통':
            grade_freq_qs = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(major_group=major_group_query) \
                .filter(admission1__admission1__contains=admission1['admission1']) \
                .values_list(Floor('ko_en_math_soc_sci_100')) \
                .annotate(student_grade_count=Count(Floor('ko_en_math_soc_sci_100')))
        else:
            grade_freq_qs = Student.objects \
                .filter(entrance_year=entrance_year_query) \
                .filter(major_group=major_group_query) \
                .filter(admission1__admission1__contains=admission1['admission1']) \
                .values_list(Floor('ko_en_math_soc_100')) \
                .annotate(student_grade_count=Count(Floor('ko_en_math_soc_100')))

        for data in grade_freq_qs:
            grade_column1_table[int(data[0] - 1)][idx + 1] = data[1]

        admission1_list.append(admission1['admission1'])

    for row in grade_column1_table:
        row[5] = sum(row[1:5])
        for i in range(1, 6):
            sum_list[i] += row[i]
    grade_column1_table.append(sum_list)

    # 계열, 전형기준 등급분포(table chart)2
    grade_column2_table = []
    for i in range(0, 8):
        grade_column2_table.append([str(i + 1), grade_column1_table[i][5], 0, 0])

    for row in grade_column2[1:]:
        grade_column2_table[int(row[0]) - 1][2] = row[1]

    for i in range(0, 8):
        if grade_column2_table[i][1] == 0:
            grade_column2_table[i][3] = 0
        else:
            grade_column2_table[i][3] = round((grade_column2_table[i][2] / grade_column2_table[i][1])*100, 1)

    #계열, 전형, 등급기준 지원대학 현황(bar chart) - 지원대학 사례 순위
    univ_name_list = []
    univ_freq_list = []
    univ_name_qs = UnivName.objects.all()

    if str(MajorGroup.objects.get(pk=major_group_query)) == '자연':
        univ_freq_qs = Student.objects\
                           .filter(entrance_year=entrance_year_query) \
                           .filter(major_group=major_group_query) \
                           .filter(admission1__admission1__contains=admission1_query) \
                           .filter(ko_en_math_sci_100__gte=gte_query) \
                           .filter(ko_en_math_sci_100__lt=lt_query)\
                           .values_list('univ_name')\
                           .annotate(univ_count=Count('univ_name'))\
                           .order_by('-univ_count')[:25]
    elif str(MajorGroup.objects.get(pk=major_group_query)) == '공통':
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

    #계열, 전형, 등급기준 지원대학 현황(bar chart) - 지원 대학 합격/충원합격/불합격 현황
    univ_pass_freq_list = []
    univ_supplement_freq_list = []
    univ_fail_freq_list = []
    univ_psf_bar = [['대학명', '합격', {'role': 'style'} , '충원합격', {'role': 'style'}, '불합격', {'role': 'style'}]]

    for univ in univ_name_list:
        univ_name = univ_name_qs.get(univ_name=univ)

        if str(MajorGroup.objects.get(pk=major_group_query)) == '자연':
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
        elif str(MajorGroup.objects.get(pk=major_group_query)) == '공통':
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

    for i in range(0, len(univ_name_list)):
        univ_psf_bar.append([
            univ_name_list[i],
            univ_pass_freq_list[i],
            'stroke-color: #000000; stroke-width: 1; opacity: 0.5',
            univ_supplement_freq_list[i],
            'stroke-color: #000000; stroke-width: 1; opacity: 0.5',
            univ_fail_freq_list[i],
            'stroke-color: #000000; stroke-width: 1; opacity: 0.5',
        ])

    context = {
        'entrance_year_item': entrance_year_qs,
        'major_group_item': major_group_qs,
        'admission1_item': admission1_qs,

        'current_entrance_year': entrance_year_query,
        'current_major_group': int(major_group_query),
        'current_major_group_str': str(MajorGroup.objects.get(pk=major_group_query)),
        'current_admission1': admission1_query,
        'current_gte': int(gte_query),

        'grade_column2': grade_column2,
        'grade_column2_table': grade_column2_table,
        'univ_psf_bar': univ_psf_bar,
    }
    return render(request, template, context)


@login_required(login_url="login")
def univ_region(request):
    template = "statistic/univ_region.html"

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
def univ_region_result(request):
    template = "statistic/univ_region_result.html"

    entrance_year_qs = Student.objects.values('entrance_year').order_by('entrance_year').distinct()
    major_group_qs = MajorGroup.objects.order_by('major_group').distinct()
    univ_region_qs = UnivRegion.objects.order_by('univ_region').distinct()

    entrance_year_query = request.GET.get('entrance_year')
    major_group_query = request.GET.get('major_group')
    univ_region_query = request.GET.get('univ_region')
    admission1_query = request.GET.get('admission1')

    # 계열, 대학지역기준 등급분포(column chart)
    grade_list = []
    grade_freq_list = []
    grade_column2 = [['등급', '사례수', {'role': 'style'}]]

    if str(MajorGroup.objects.get(pk=major_group_query)) == '자연':
        grade_freq_qs = Student.objects \
            .filter(entrance_year=entrance_year_query) \
            .filter(major_group=major_group_query) \
            .filter(univ_region=univ_region_query) \
            .values_list(Floor('ko_en_math_sci_100')) \
            .annotate(student_grade_count=Count(Floor('ko_en_math_sci_100')))
    elif str(MajorGroup.objects.get(pk=major_group_query)) == '공통':
        grade_freq_qs = Student.objects \
            .filter(entrance_year=entrance_year_query) \
            .filter(major_group=major_group_query) \
            .filter(univ_region=univ_region_query) \
            .values_list(Floor('ko_en_math_soc_sci_100')) \
            .annotate(student_grade_count=Count(Floor('ko_en_math_soc_sci_100')))
    else:
        grade_freq_qs = Student.objects \
            .filter(entrance_year=entrance_year_query) \
            .filter(major_group=major_group_query) \
            .filter(univ_region=univ_region_query) \
            .values_list(Floor('ko_en_math_soc_100')) \
            .annotate(student_grade_count=Count(Floor('ko_en_math_soc_100')))

    for grade in grade_freq_qs:
        grade_list.append(int(grade[0]))
        grade_freq_list.append(grade[1])

    for i in range(0, len(grade_list)):
        grade_column2.append([
            grade_list[i],
            grade_freq_list[i],
            'color: #3162C7; stroke-color: #000000; stroke-width: 2; opacity: 0.8',
        ])

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
    univ_psf_bar = [['대학명', '합격', {'role': 'style'}, '충원합격', {'role': 'style'}, '불합격', {'role': 'style'}]]

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

    for i in range(0, len(univ_name_list)):
        univ_psf_bar.append([
            univ_name_list[i],
            univ_pass_freq_list[i],
            'stroke-color: #000000; stroke-width: 1; opacity: 0.5',
            univ_supplement_freq_list[i],
            'stroke-color: #000000; stroke-width: 1; opacity: 0.5',
            univ_fail_freq_list[i],
            'stroke-color: #000000; stroke-width: 1; opacity: 0.5',
        ])

    context = {
        'entrance_year_item': entrance_year_qs,
        'major_group_item': major_group_qs,
        'univ_region_item': univ_region_qs,

        'current_entrance_year': int(entrance_year_query),
        'current_major_group': int(major_group_query),
        'current_major_group_str': str(MajorGroup.objects.get(pk=major_group_query)),
        'current_univ_region': int(univ_region_query),
        'current_univ_region_str': str(UnivRegion.objects.get(pk=univ_region_query)),
        'current_admission1': admission1_query,

        'grade_column2': grade_column2,
        'univ_psf_bar': univ_psf_bar,
    }
    return render(request, template, context)


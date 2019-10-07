import csv, io
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from .models import Student
from .models import UnivGroup
from .models import UnivRegion
from .models import MajorGroup
from .models import UnivName
from .models import UnivMajor
from .models import Admission1
from .models import Admission2
from .models import Admission3
from .models import Personnel


def analysis1(request):
    template = "analysis/grade_interval_search.html"

    major_group_qs = MajorGroup.objects.all().order_by('major_group')
    univ_region_qs = UnivRegion.objects.all().order_by('univ_region')

    context = {
        'major_group_item': major_group_qs,
        'univ_region_item': univ_region_qs
    }
    return render(request, template, context)


def search1(request):
    template = "analysis/grade_interval_search.html"

    major_group_qs = MajorGroup.objects.all().order_by('major_group')
    univ_region_qs = UnivRegion.objects.all().order_by('univ_region')
    student_qs = Student.objects.all()
    final_step = ['합격', '충원합격', '불합격']

    major_group_query = request.GET.get('major_group')
    univ_region_query = request.GET.get('univ_region')
    ko_en_math_soc_or_sci_100_min_query = request.GET.get('ko_en_math_soc_or_sci_100_min')
    ko_en_math_soc_or_sci_100_max_query = request.GET.get('ko_en_math_soc_or_sci_100_max')

    if major_group_query != '' and major_group_query is not None:
        student_qs = student_qs.filter(major_group=major_group_query)

    if univ_region_query != '' and univ_region_query is not None:
        if univ_region_query == '지역 전체':
            student_qs = student_qs
        else:
            student_qs = student_qs.filter(univ_region=univ_region_query)

    if ko_en_math_soc_or_sci_100_min_query != '' and ko_en_math_soc_or_sci_100_min_query is not None:
        if major_group_qs.get(pk=major_group_query) == '자연':
            student_qs = student_qs.filter(ko_en_math_sci_100__gte=ko_en_math_soc_or_sci_100_min_query)
        elif major_group_qs.get(pk=major_group_query) == '공통':
            student_qs = student_qs.filter(ko_en_math_soc_sci_100__gte=ko_en_math_soc_or_sci_100_min_query)
        else:
            student_qs = student_qs.filter(ko_en_math_soc_100__gte=ko_en_math_soc_or_sci_100_min_query)

    if ko_en_math_soc_or_sci_100_max_query != '' and ko_en_math_soc_or_sci_100_max_query is not None:
        if major_group_qs.get(pk=major_group_query) == '자연':
            student_qs = student_qs.filter(ko_en_math_sci_100__lte=ko_en_math_soc_or_sci_100_max_query)
        elif major_group_qs.get(pk=major_group_query) == '공통':
            student_qs = student_qs.filter(ko_en_math_soc_sci_100__lte=ko_en_math_soc_or_sci_100_max_query)
        else:
            student_qs = student_qs.filter(ko_en_math_soc_100__lte=ko_en_math_soc_or_sci_100_max_query)

    if major_group_qs.get(pk=major_group_query) == '자연':
        student_qs = student_qs.order_by('-final_step', 'ko_en_math_sci_100')
    elif major_group_qs.get(pk=major_group_query) == '공통':
        student_qs = student_qs.order_by('-final_step', 'ko_en_math_soc_sci_100')
    else:
        student_qs = student_qs.order_by('-final_step', 'ko_en_math_soc_100')

    context = {
        'queryset': student_qs,
        'major_group_item': major_group_qs,
        'univ_region_item': univ_region_qs,
        'current_major_group': int(major_group_query),
        'current_univ_region': int(univ_region_query),
        'current_major_group_str': str(major_group_qs.get(pk=major_group_query)),
        'current_ko_en_math_soc_or_sci_100_min': ko_en_math_soc_or_sci_100_min_query,
        'current_ko_en_math_soc_or_sci_100_max': ko_en_math_soc_or_sci_100_max_query,
        'final_step': final_step
    }
    return render(request, template, context)


def analysis2(request):
    template = "analysis/univ_major_search.html"

    major_group_qs = MajorGroup.objects.all().order_by('major_group')

    context = {
        'major_group_item': major_group_qs
    }
    return render(request, template, context)


def search2(request):
    template = "analysis/univ_major_search.html"

    major_group_qs = MajorGroup.objects.all().order_by('major_group')
    univ_major_qs = UnivMajor.objects.all()
    student_qs = Student.objects.all()
    final_step = ['합격', '충원합격', '불합격']

    major_group_query = request.GET.get('major_group')
    univ_major_query = request.GET.get('univ_major')
    ko_en_math_soc_or_sci_100_min_query = request.GET.get('ko_en_math_soc_or_sci_100_min')
    ko_en_math_soc_or_sci_100_max_query = request.GET.get('ko_en_math_soc_or_sci_100_max')

    if major_group_query != '' and major_group_query is not None:
        student_qs = student_qs.filter(major_group=major_group_query)

    if univ_major_query != '' and univ_major_query is not None:
        univ_major_qs = univ_major_qs.filter(univ_major__icontains=univ_major_query)

        union_qs = Student.objects.filter(univ_major='0')
        for univ_major in univ_major_qs:
            union_qs = union_qs | student_qs.filter(univ_major=univ_major.id)
        student_qs = union_qs

    if ko_en_math_soc_or_sci_100_min_query != '' and ko_en_math_soc_or_sci_100_min_query is not None:
        if major_group_qs.get(pk=major_group_query) == '자연':
            student_qs = student_qs.filter(ko_en_math_sci_100__gte=ko_en_math_soc_or_sci_100_min_query)
        elif major_group_qs.get(pk=major_group_query) == '공통':
            student_qs = student_qs.filter(ko_en_math_soc_sci_100__gte=ko_en_math_soc_or_sci_100_min_query)
        else:
            student_qs = student_qs.filter(ko_en_math_soc_100__gte=ko_en_math_soc_or_sci_100_min_query)

    if ko_en_math_soc_or_sci_100_max_query != '' and ko_en_math_soc_or_sci_100_max_query is not None:
        if major_group_qs.get(pk=major_group_query) == '자연':
            student_qs = student_qs.filter(ko_en_math_sci_100__lte=ko_en_math_soc_or_sci_100_max_query)
        elif major_group_qs.get(pk=major_group_query) == '공통':
            student_qs = student_qs.filter(ko_en_math_soc_sci_100__lte=ko_en_math_soc_or_sci_100_max_query)
        else:
            student_qs = student_qs.filter(ko_en_math_soc_100__lte=ko_en_math_soc_or_sci_100_max_query)

    if major_group_qs.get(pk=major_group_query) == '자연':
        student_qs = student_qs.order_by('-final_step', 'ko_en_math_sci_100')
    elif major_group_qs.get(pk=major_group_query) == '공통':
        student_qs = student_qs.order_by('-final_step', 'ko_en_math_soc_sci_100')
    else:
        student_qs = student_qs.order_by('-final_step', 'ko_en_math_soc_100')

    context = {
        'queryset': student_qs,
        'major_group_item': major_group_qs,
        'current_major_group': int(major_group_query),
        'current_univ_major': univ_major_query,
        'current_major_group_str': str(major_group_qs.get(pk=major_group_query)),
        'current_ko_en_math_soc_or_sci_100_min': ko_en_math_soc_or_sci_100_min_query,
        'current_ko_en_math_soc_or_sci_100_max': ko_en_math_soc_or_sci_100_max_query,
        'final_step': final_step
    }
    return render(request, template, context)


def analysis3(request):
    template = "analysis/advanced_search.html"

    major_group_item = ['인문', '자연', '예체능', '공통']
    univ_region_item = ['지역 전체', '강원', '경기', '경남', '경북', '광주', '대구', '대전', '부산',
                        '서울', '세종', '울산', '인천', '전남', '전북', '제주', '충남', '충북']
    admission1_item = ['종합', '교과']

    context = {
        'major_group_item': major_group_item,
        'univ_region_item': univ_region_item,
        'admission1_item': admission1_item,
    }
    return render(request, template, context)


def search3(request):
    template = "analysis/advanced_search.html"

    major_group_item = ['인문', '자연', '예체능', '공통']
    univ_region_item = ['지역 전체', '강원', '경기', '경남', '경북', '광주', '대구', '대전', '부산',
                        '서울', '세종', '울산', '인천', '전남', '전북', '제주', '충남', '충북']
    admission1_item = ['종합', '교과']
    final_step = ['합격', '충원합격', '불합격']

    qs = Student.objects.all()
    major_group_query = request.GET.get('major_group')
    univ_region_query = request.GET.get('univ_region')
    univ_name_query = request.GET.get('univ_name')
    univ_major_query = request.GET.get('univ_major')
    admission1_query = request.GET.get('admission1')
    admission2_query = request.GET.get('admission2')
    ko_en_math_soc_or_sci_100_min_query = request.GET.get('ko_en_math_soc_or_sci_100_min')
    ko_en_math_soc_or_sci_100_max_query = request.GET.get('ko_en_math_soc_or_sci_100_max')

    if major_group_query != '' and major_group_query is not None:
        qs = qs.filter(major_group=major_group_query)

    if univ_region_query != '' and univ_region_query is not None:
        if univ_region_query == '지역 전체':
            qs = qs
        else:
            qs = qs.filter(univ_region=univ_region_query)

    if univ_name_query != '' and univ_name_query is not None:
        if univ_name_query == '':
            qs = qs
        else:
            qs = qs.filter(univ_name__icontains=univ_name_query)

    if univ_major_query != '' and univ_major_query is not None:
        if univ_major_query == '':
            qs = qs
        else:
            qs = qs.filter(univ_major__icontains=univ_major_query)

    if admission1_query != '' and admission1_query is not None:
        if admission1_query == '':
            qs = qs
        else:
            qs = qs.filter(admission1=admission1_query)

    if admission2_query != '' and admission2_query is not None:
        if admission2_query == '':
            qs = qs
        else:
            qs = qs.filter(admission2__icontains=admission2_query)

    if ko_en_math_soc_or_sci_100_min_query != '' and ko_en_math_soc_or_sci_100_min_query is not None:
        if major_group_query == '자연':
            qs = qs.filter(ko_en_math_sci_100__gte=ko_en_math_soc_or_sci_100_min_query)
        elif major_group_query == '공통':
            qs = qs.filter(ko_en_math_soc_sci_100__gte=ko_en_math_soc_or_sci_100_min_query)
        else:
            qs = qs.filter(ko_en_math_soc_100__gte=ko_en_math_soc_or_sci_100_min_query)

    if ko_en_math_soc_or_sci_100_max_query != '' and ko_en_math_soc_or_sci_100_max_query is not None:
        if major_group_query == '자연':
            qs = qs.filter(ko_en_math_sci_100__lte=ko_en_math_soc_or_sci_100_max_query)
        elif major_group_query == '공통':
            qs = qs.filter(ko_en_math_soc_sci_100__lte=ko_en_math_soc_or_sci_100_max_query)
        else:
            qs = qs.filter(ko_en_math_soc_100__lte=ko_en_math_soc_or_sci_100_max_query)

    if major_group_query == '자연':
        qs = qs.order_by('-final_step', 'ko_en_math_sci_100')
    elif major_group_query == '공통':
        qs = qs.order_by('-final_step', 'ko_en_math_soc_sci_100')
    else:
        qs = qs.order_by('-final_step', 'ko_en_math_soc_100')

    context = {
        'queryset': qs,
        'major_group_item': major_group_item,
        'univ_region_item': univ_region_item,
        'admission1_item': admission1_item,
        'current_major_group': major_group_query,
        'current_univ_region': univ_region_query,
        'current_univ_name': univ_name_query,
        'current_univ_major': univ_major_query,
        'current_admission1': admission1_query,
        'current_admission2': admission2_query,
        'current_ko_en_math_soc_or_sci_100_min': ko_en_math_soc_or_sci_100_min_query,
        'current_ko_en_math_soc_or_sci_100_max': ko_en_math_soc_or_sci_100_max_query,
        'final_step': final_step
    }
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def univ_data_upload1(request):
    template = "univ_data_upload.html"

    prompt = {
        'order': 'univ_data.csv uploader1(univ_group, univ_region, major_group upload)'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    # univ_group, univ_region, major_group upload
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = UnivGroup.objects.update_or_create(
            univ_group=column[2],
        )
        _, created = UnivRegion.objects.update_or_create(
            univ_region=column[3],
        )
        _, created = MajorGroup.objects.update_or_create(
            major_group=column[4],
        )

    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def univ_data_upload2(request):
    template = "univ_data_upload.html"

    prompt = {
        'order': 'univ_data.csv uploader2(univ_name upload)'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    # univ_name upload
    univ_group_qs = UnivGroup.objects.all()
    univ_region_qs = UnivRegion.objects.all()
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        univ_group_id = univ_group_qs.filter(univ_group=column[2])[0]
        univ_region_id = univ_region_qs.filter(univ_region=column[3])[0]
        _, created = UnivName.objects.update_or_create(
            univ_name=column[5],
            univ_group=univ_group_id,
            univ_region=univ_region_id
        )

    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def univ_data_upload3(request):
    template = "univ_data_upload.html"

    prompt = {
        'order': 'univ_data.csv uploader3(univ_major upload)'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    # univ_major upload
    major_group_qs = MajorGroup.objects.all()
    univ_name_qs = UnivName.objects.all()
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        major_group_id = major_group_qs.filter(major_group=column[4])[0]
        univ_name_id = univ_name_qs.filter(univ_name=column[5])[0]
        _, created = UnivMajor.objects.update_or_create(
            univ_major=column[6],
            major_group=major_group_id,
            univ_name=univ_name_id
        )

    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def univ_data_upload4(request):
    template = "univ_data_upload.html"

    prompt = {
        'order': 'univ_data.csv uploader4(admission1 upload)'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    # admission1 upload
    univ_name_qs = UnivName.objects.all()
    univ_major_qs = UnivMajor.objects.all()
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        univ_name_id = univ_name_qs.filter(univ_name=column[5])[0]
        univ_major_id = univ_major_qs.filter(univ_major=column[6]).filter(univ_name_id=univ_name_id)[0]
        _, created = Admission1.objects.update_or_create(
            admission1=column[7],
            univ_name=univ_name_id,
            univ_major=univ_major_id
        )

    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def univ_data_upload5(request):
    template = "univ_data_upload.html"

    prompt = {
        'order': 'univ_data.csv uploader5(admission2 upload)'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    # admission2 upload
    univ_name_qs = UnivName.objects.all()
    univ_major_qs = UnivMajor.objects.all()
    admission1_qs = Admission1.objects.all()
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        univ_name_id = univ_name_qs.filter(univ_name=column[5])[0]
        univ_major_id = univ_major_qs.filter(univ_major=column[6]).filter(univ_name_id=univ_name_id)[0]
        admission1_id = admission1_qs.filter(admission1=column[7]).filter(univ_major_id=univ_major_id) \
            .filter(univ_name_id=univ_name_id)[0]
        _, created = Admission2.objects.update_or_create(
            admission2=column[8],
            univ_name=univ_name_id,
            univ_major=univ_major_id,
            admission1=admission1_id
        )

    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def univ_data_upload6(request):
    template = "univ_data_upload.html"

    prompt = {
        'order': 'univ_data.csv uploader6(admission3 upload)'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    # admission3 upload
    univ_name_qs = UnivName.objects.all()
    univ_major_qs = UnivMajor.objects.all()
    admission1_qs = Admission1.objects.all()
    admission2_qs = Admission2.objects.all()
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        univ_name_id = univ_name_qs.filter(univ_name=column[5])[0]
        univ_major_id = univ_major_qs.filter(univ_major=column[6]).filter(univ_name_id=univ_name_id)[0]
        admission1_id = admission1_qs.filter(admission1=column[7]).filter(univ_major_id=univ_major_id) \
            .filter(univ_name_id=univ_name_id)[0]
        admission2_id = admission2_qs.filter(admission2=column[8]).filter(admission1_id=admission1_id) \
            .filter(univ_major_id=univ_major_id).filter(univ_name_id=univ_name_id)[0]
        _, created = Admission3.objects.update_or_create(
            admission3=column[9],
            univ_name=univ_name_id,
            univ_major=univ_major_id,
            admission1=admission1_id,
            admission2=admission2_id
        )

    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def univ_data_upload7(request):
    template = "univ_data_upload.html"

    prompt = {
        'order': 'univ_data.csv uploader7(personnel upload)'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    # personnel upload
    univ_name_qs = UnivName.objects.all()
    univ_major_qs = UnivMajor.objects.all()
    admission1_qs = Admission1.objects.all()
    admission2_qs = Admission2.objects.all()
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        univ_name_id = univ_name_qs.filter(univ_name=column[5])[0]
        univ_major_id = univ_major_qs.filter(univ_major=column[6]).filter(univ_name_id=univ_name_id)[0]
        admission1_id = admission1_qs.filter(admission1=column[7]).filter(univ_major_id=univ_major_id) \
            .filter(univ_name_id=univ_name_id)[0]
        admission2_id = admission2_qs.filter(admission2=column[8]).filter(admission1_id=admission1_id) \
            .filter(univ_major_id=univ_major_id).filter(univ_name_id=univ_name_id)[0]

        if column[44] == '' or column[44] == '0':
            column[44] = None

        _, created = Personnel.objects.update_or_create(
            personnel=column[44],
            univ_name=univ_name_id,
            univ_major=univ_major_id,
            admission1=admission1_id,
            admission2=admission2_id
        )

    context = {}
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def univ_data_upload8(request):
    template = "univ_data_upload.html"

    prompt = {
        'order': 'student_data.csv uploader(Student_data upload)'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    # Student_data upload
    univ_group_qs = UnivGroup.objects.all()
    univ_region_qs = UnivRegion.objects.all()
    major_group_qs = MajorGroup.objects.all()
    univ_name_qs = UnivName.objects.all()
    univ_major_qs = UnivMajor.objects.all()
    admission1_qs = Admission1.objects.all()
    admission2_qs = Admission2.objects.all()
    admission3_qs = Admission3.objects.all()
    personnel_qs = Personnel.objects.all()
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        univ_group_id = univ_group_qs.filter(univ_group=column[2])[0]
        univ_region_id = univ_region_qs.filter(univ_region=column[3])[0]
        major_group_id = major_group_qs.filter(major_group=column[4])[0]
        univ_name_id = univ_name_qs.filter(univ_name=column[5])[0]
        univ_major_id = univ_major_qs.filter(univ_major=column[6]).filter(univ_name_id=univ_name_id)[0]
        admission1_id = admission1_qs.filter(admission1=column[7]).filter(univ_major_id=univ_major_id) \
            .filter(univ_name_id=univ_name_id)[0]
        admission2_id = admission2_qs.filter(admission2=column[8]).filter(admission1_id=admission1_id) \
            .filter(univ_major_id=univ_major_id).filter(univ_name_id=univ_name_id)[0]
        admission3_id = admission3_qs.filter(admission3=column[9]).filter(admission2_id=admission2_id) \
            .filter(admission1_id=admission1_id).filter(univ_major_id=univ_major_id) \
            .filter(univ_name_id=univ_name_id)[0]

        if column[44] == '' or column[44] == '0':
            column[44] = None

        personnel_id = personnel_qs.filter(personnel=column[44]).filter(admission2_id=admission2_id) \
            .filter(admission1_id=admission1_id).filter(univ_major_id=univ_major_id) \
            .filter(univ_name_id=univ_name_id)[0]

        if column[11] == '' or column[11] == '0':
            column[11] = None

        if column[40] == '' or column[40] == '0':
            column[40] = None

        if column[42] == '' or column[42] == '0':
            column[42] = None

        if column[43] == '' or column[43] == '0':
            column[43] = None

        _, created = Student.objects.update_or_create(
            entrance_year=column[0],
            student_region=column[1],
            univ_group=univ_group_id,
            univ_region=univ_region_id,
            major_group=major_group_id,
            univ_name=univ_name_id,
            univ_major=univ_major_id,
            admission1=admission1_id,
            admission2=admission2_id,
            admission3=admission3_id,
            grade=column[10],
            univ_score=column[11],
            korean=column[12],
            english=column[13],
            mathematics=column[14],
            society=column[15],
            science=column[16],
            all_subject_100=column[17],
            all_subject_244=column[18],
            all_subject_433=column[19],
            all_subject_235=column[20],
            ko_en_math_soc_sci_100=column[21],
            ko_en_math_soc_sci_244=column[22],
            ko_en_math_soc_sci_334=column[23],
            ko_en_math_soc_sci_433=column[24],
            ko_en_math_100=column[25],
            ko_en_math_soc_100=column[26],
            ko_en_math_soc_244=column[27],
            ko_en_math_soc_334=column[28],
            ko_en_math_soc_433=column[29],
            ko_en_math_soc_370=column[30],
            ko_en_soc_100=column[31],
            ko_en_soc_244=column[32],
            ko_en_math_sci_100=column[33],
            ko_en_math_sci_244=column[34],
            ko_en_math_sci_334=column[35],
            ko_en_math_sci_433=column[36],
            ko_en_math_sci_370=column[37],
            en_math_sci_100=column[38],
            en_math_sci_244=column[39],
            first_step=column[40],
            final_step=column[41],
            fail_reason=column[42],
            candidate_rank=column[43],
            personnel=personnel_id
        )
    context = {}
    return render(request, template, context)
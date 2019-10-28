import csv, io
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.views.generic.base import TemplateView
from analysis.models import *

class HomeView(TemplateView):
    template_name = 'home.html'


def load_univ_name(request):
    template = "dropdown_univ_name.html"
    univ_region = request.GET.get('univ_region')
    univ_name_qs = UnivName.objects.filter(univ_region=univ_region).order_by('univ_name')
    return render(request, template, {'univ_name_item': univ_name_qs})


def load_univ_major(request):
    template = "dropdown_univ_major.html"
    major_group = request.GET.get('major_group')
    univ_name = request.GET.get('univ_name')
    univ_major_qs = UnivMajor.objects.filter(univ_name=univ_name).filter(major_group=major_group).order_by('univ_major')
    return render(request, template, {'univ_major_item': univ_major_qs})


def load_admission1(request):
    template = "dropdown_admission1.html"
    univ_major = request.GET.get('univ_major')
    admission1_qs = Admission1.objects.filter(univ_major=univ_major)
    return render(request, template, {'admission1_item': admission1_qs})


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
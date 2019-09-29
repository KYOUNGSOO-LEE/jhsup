import csv, io
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import ibsi


def analysis1(request):
    qs = ibsi.objects.all()
    gubun2_query = request.GET.get('gubun2')
    print(gubun2_query)
    if gubun2_query != '' and gubun2_query is not None:
        qs = qs.filter(gubun2=gubun2_query)

    context={
        'queryset' : qs
    }
    return render(request, 'analysis/analysis1.html', context)

def analysis2(request):
    return render(request, 'analysis/analysis2.html')
# Create your views here.

@permission_required('admin.can_add_log_entry')
def ibsi_upload(request):
    template = "ibsi_upload.html"

    prompt = {
        'order': 'ibsi.csv uploader'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter = ',', quotechar="|"):

        for i in range(0, 45):
            if column[i] == '' or column[i] == '0':
                column[i] = None

        _, created = ibsi.objects.update_or_create(
            ibsi_year=column[0],
            resion1=column[1],
            gubun1=column[2],
            resion2=column[3],
            gubun2=column[4],
            univ_name=column[5],
            univ_major=column[6],
            admission1=column[7],
            admission2=column[8],
            admission3=column[9],
            grade=column[10],
            myscore=column[11],
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
            num_students=column[44]
        )
    context = {}
    return render(request, template, context)

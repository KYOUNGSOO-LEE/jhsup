from django.shortcuts import render


def analysis1(request):
    return render(request, 'analysis/analysis1.html')

def analysis2(request):
    return render(request, 'analysis/analysis2.html')
# Create your views here.

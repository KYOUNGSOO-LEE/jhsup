from django import forms
from crispy_forms.helper import FormHelper
from .models import *


class AdvancedForm(forms.Form):
    helper = FormHelper()
    helper.form_show_labels = False

    major_group = forms.ModelChoiceField(queryset=MajorGroup.objects.all().order_by('major_group'), empty_label='계열')
    univ_region = forms.ModelChoiceField(queryset=UnivRegion.objects.all().order_by('univ_region'), empty_label='지역')
    univ_name = forms.ModelChoiceField(queryset=UnivName.objects.none(), empty_label='대학명')
    univ_major = forms.ModelChoiceField(queryset=UnivMajor.objects.none(), empty_label='학과명')
    admission1 = forms.ModelChoiceField(queryset=Admission1.objects.none(), empty_label='전형')

"""
class AdvancedForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False

    class Meta:
        model = Student
        fields = ('major_group',
                  'univ_region',
                  'univ_name',
                  'univ_major',
                  'admission1',
        )
"""
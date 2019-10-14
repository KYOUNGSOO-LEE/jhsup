from django import forms
from crispy_forms.helper import FormHelper
from .models import *


class AdvancedForm(forms.Form):
    helper = FormHelper()
    helper.form_show_labels = False

    major_group = forms.ModelChoiceField(queryset=MajorGroup.objects.all().order_by('major_group'), empty_label='계열')
    univ_region = forms.ModelChoiceField(queryset=UnivRegion.objects.all().order_by('univ_region'), empty_label='지역')
    univ_name = forms.ChoiceField()
    univ_major = forms.ChoiceField()
    admission1 = forms.ChoiceField()

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
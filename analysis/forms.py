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
    admission2 = forms.ModelChoiceField(queryset=Admission2.objects.none(), empty_label='세부전형')

    def __init__(self, major_group, univ_region, univ_name, univ_major, admission1,  *args, **kwargs):
        super(AdvancedForm, self).__init__(*args, **kwargs)

        if univ_region != '':
            self.fields['univ_name'].queryset = UnivName.objects.filter(univ_region=univ_region)
        else:
            self.fields['univ_name'].queryset = UnivName.objects.none()

        if univ_name != '':
            self.fields['univ_major'].queryset = UnivMajor.objects.filter(major_group=major_group).filter(univ_name=univ_name)
        else:
            self.fields['univ_major'].queryset = UnivMajor.objects.none()

        if univ_major != '':
            self.fields['admission1'].queryset = Admission1.objects.filter(univ_major=univ_major)
        else:
            self.fields['admission1'].queryset = Admission1.objects.none()

        if admission1 != '':
            self.fields['admission2'].queryset = Admission2.objects.filter(admission1=admission1)
        else:
            self.fields['admission2'].queryset = Admission2.objects.none()
from django import forms
from crispy_forms.helper import FormHelper

from .models import *


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

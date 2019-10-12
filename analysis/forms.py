from django import forms
from .models import *


class AdvancedForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('major_group',
                  'univ_region',
                  'univ_name',
                  'univ_major',
                  'admission1',
                  'admission2',
                  )
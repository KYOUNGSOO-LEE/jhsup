from django import forms
from .models import *


class AdvancedForm(forms.ModelForm):
    class Meta:
        model = UnivName
        fields = ('univ_region', 'univ_name')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['univ_name'].queryset = UnivName.objects.none()

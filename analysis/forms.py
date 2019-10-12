from django import forms
from .models import *


class AdvancedForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('univ_region', 'univ_name', 'univ_major',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['univ_name'].queryset = UnivName.objects.none()
            self.fields['univ_major'].queryset = UnivMajor.objects.none()

            if 'univ_region' in self.data:
                try:
                    univ_region = int(self.data.get('univ_region'))
                    self.fields['univ_name'].queryset = UnivName.objects.filter(univ_region=univ_region).order_by('univ_name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty UnivName queryset
            elif self.instance.pk:
                self.fields['univ_name'].queryset = self.instance.univ_region.univ_name_set.order_by('univ_name')

            if 'univ_name' in self.data:
                try:
                    univ_name = int(self.data.get('univ_name'))
                    self.fields['univ_major'].queryset = UnivMajor.objects.filter(univ_name=univ_name).order_by('univ_major')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty UnivName queryset
            elif self.instance.pk:
                self.fields['univ_major'].queryset = self.instance.univ_name.univ_major_set.order_by('univ_major')
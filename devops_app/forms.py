from devops_app.models import Devops
from django import forms


class DevopsUploadForm(forms.ModelForm):
    class Meta:
        model = Devops
        widgets = {
            'Date': forms.DateInput(attrs={'type': 'date'}),
        }
        fields = ['name', 'vedio_file', 'choose_month', 'Date']
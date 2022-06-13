from django import forms
from .models import ClassOfBusiness

class classOfBusinessForm(forms.ModelForm):
    class Meta:
        model = ClassOfBusiness
        fields = "__all__"
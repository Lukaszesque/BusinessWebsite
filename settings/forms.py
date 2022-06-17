from django import forms
from django.forms import TextInput
from .models import ClassOfBusiness

class classOfBusinessForm(forms.ModelForm):
    class Meta:
        model = ClassOfBusiness
        fields = ["classOfBusiness_text"]
        labels = {"classOfBusiness_text": "Class of Business name"}
        widgets = {
            'classOfBusiness_text': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Type here..."
            }) 
        }

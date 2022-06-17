<<<<<<< HEAD
from django.forms import ModelForm
from settings.models import ClassOfBusiness

class classOfBusinessForm(ModelForm):
    class Meta:
        model = ClassOfBusiness
        fields = ['classOfBusiness_text']

form = classOfBusinessForm()
=======
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
>>>>>>> d00e502c16b3c7f73a79f879c2483d7cfb08461e

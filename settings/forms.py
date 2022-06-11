from django import forms

class classOfBusinessForm(forms.Form):
    classOfBusinessName = forms.CharField(label='Class of business name', max_length=200)

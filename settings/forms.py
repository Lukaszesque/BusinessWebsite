from django.forms import ModelForm
from settings.models import ClassOfBusiness

class classOfBusinessForm(ModelForm):
    class Meta:
        model = ClassOfBusiness
        fields = ['classOfBusiness_text']

form = classOfBusinessForm()

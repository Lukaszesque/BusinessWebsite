from msilib.schema import Class
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator

from settings.models import ClassOfBusiness
from settings.forms import classOfBusinessForm


#To implement:
#--validation for delete feature
#--implement pagination
#--django tests
#--favicon
#--implement services

def index(request):
    context = {}

    context["dataset"] = ClassOfBusiness.objects.all()

    return render(request, "settings/classOfBusiness/index.html", context)

def add(request):
    context={}
    
    form = classOfBusinessForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Class of Business added successfully!")
        return HttpResponseRedirect(reverse('index'))

    context['form'] = form
    return render(request, "settings/classOfBusiness/add.html", context)

def delete(request, id):
    classToDelete = ClassOfBusiness.objects.get(id=id)
    classToDelete.delete()
    return HttpResponseRedirect(reverse('index'))

def edit(request, id):
    classToEdit = ClassOfBusiness.objects.get(id=id)
    context = {
        'classToEdit': classToEdit,
    }

    return render(request, "settings/classOfBusiness/edit.html", context)

def updateRecord(request, id):
    updatedClass = request.POST['editedClassName']
    classOfBusiness = ClassOfBusiness.objects.get(id = id)
    classOfBusiness.classOfBusiness_text = updatedClass
    classOfBusiness.save()
    return HttpResponseRedirect(reverse('index'))

    

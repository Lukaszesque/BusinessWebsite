from msilib.schema import Class
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.contrib import messages
from django.urls import reverse

from settings.models import ClassOfBusiness
from settings.forms import classOfBusinessForm

#To refactor: 
#--abstract URLS into a more favourable format
#--refactor the Static files
#--use the url config to reduce the length of urls passed down
#--make the name of the views shorter
#--departments view is faulty
#--validation for edit/delete feature
#--implement pagination
#--amend Add CoB to a simpler approach of form implementation like you did in Edit

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
        return HttpResponseRedirect(reverse('settingsClassOfBusiness'))

    context['form'] = form
    return render(request, "settings/classOfBusiness/add.html", context)

def deleteClassOfBusiness(request, id):
    classToDelete = ClassOfBusiness.objects.get(id=id)
    classToDelete.delete()
    return HttpResponseRedirect(reverse('settingsClassOfBusiness'))

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
    return HttpResponseRedirect(reverse('settingsClassOfBusiness'))

    

from msilib.schema import Class
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.contrib import messages
from django.urls import reverse

from settings.models import ClassOfBusiness
from settings.forms import classOfBusinessForm
from settings.models import ClassOfBusiness

#To refactor: 
#--styling for class of business edit templates
#--get rid of index and make default CoB index
#--refactor the Static files
#--use the url config to reduce the length of urls passed down
#--make the name of the views shorter
#--departments view is faulty
#--validation for edit/delete feature
#--implement pagination
#--amend Add CoB to a simpler approach of form implementation like you did in Edit


def index(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def settingsClassOfBusiness(request):
    context = {}

    context["dataset"] = ClassOfBusiness.objects.all()

    return render(request, "settings/classOfBusiness.html", context)

def settingsAddNewClassOfBusiness(request):
    context={}
    
    form = classOfBusinessForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Class of Business added successfully!")
        return redirect("/settings/classOfBusiness")

    context['form'] = form
    return render(request, "settings/classOfBusinessAdd.html", context)

def deleteClassOfBusiness(request, id):
    classToDelete = ClassOfBusiness.objects.get(id=id)
    classToDelete.delete()
    return HttpResponseRedirect(reverse('settingsClassOfBusiness'))

def edit(request, id):
    classToEdit = ClassOfBusiness.objects.get(id=id)
    context = {
        'classToEdit': classToEdit,
    }

    return render(request, "settings/edit.html", context)

def updateRecord(request, id):
    updatedClass = request.POST['editedClassName']
    classOfBusiness = ClassOfBusiness.objects.get(id = id)
    classOfBusiness.classOfBusiness_text = updatedClass
    classOfBusiness.save()
    return HttpResponseRedirect(reverse('settingsClassOfBusiness'))

    

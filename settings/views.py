from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from settings.models import ClassOfBusiness
from .forms import classOfBusinessForm
from .models import ClassOfBusiness
import logging

# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def settingsDepartments(request):
    template = loader.get_template("settings/departments.html")
    context = {}
    return HttpResponse(template.render(context, request))

def settingsClassOfBusiness(request):
<<<<<<< HEAD
    allClassesOfBusiness = ClassOfBusiness.objects.all()
    template = loader.get_template("settings/classOfBusiness.html")
    context = {  
        'allClassesOfBusiness': allClassesOfBusiness,
    }

    # if request.method == 'POST':
    #     form = classOfBusinessForm(request.POST)
    #     if form.is_valid():
    #         logging.info("great success")
    #         return HttpResponseRedirect('thanks!')
    #     else:
    #         form = classOfBusinessForm()
=======

    context = {}

    context["dataset"] = ClassOfBusiness.objects.all()
>>>>>>> d00e502c16b3c7f73a79f879c2483d7cfb08461e

    return render(request, "settings/classOfBusiness.html", context)

def settingsAddNewClassOfBusiness(request):
    context={}

    form = classOfBusinessForm(request.POST or None)
    if form.is_valid():
        form.save();

    context['form'] = form
    return render(request, "settings/classOfBusinessAdd.html", context)

def detail(request, classOfBusiness_id):
    return HttpResponse("You're looking at class of business %s." %classOfBusiness_id)

def results(request, classOfBusiness_id):
    response = "You're looking at the voting results of class of business %s."
    return HttpResponse(response % classOfBusiness_id)

def vote(request, classOfBusiness_id):
    return HttpResponse("You're voting on class of business %s." %classOfBusiness_id)
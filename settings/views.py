from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib import messages

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
    context = {}

    context["dataset"] = ClassOfBusiness.objects.all()

    return render(request, "settings/classOfBusiness.html", context)

def settingsAddNewClassOfBusiness(request):
    context={}
    
    form = classOfBusinessForm(request.POST or None)
    if form.is_valid():
        form.save();
        messages.success(request, "Class of Business added successfully!")
        return redirect("/settings/classOfBusiness");

    context['form'] = form
    return render(request, "settings/classOfBusinessAdd.html", context)

def detail(request, classOfBusiness_id):
    return HttpResponse("You're looking at class of business %s." %classOfBusiness_id)

def results(request, classOfBusiness_id):
    response = "You're looking at the voting results of class of business %s."
    return HttpResponse(response % classOfBusiness_id)

def vote(request, classOfBusiness_id):
    return HttpResponse("You're voting on class of business %s." %classOfBusiness_id)
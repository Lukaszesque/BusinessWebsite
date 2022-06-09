from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def settingsIndex(request):
    template = loader.get_template("settings/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def detail(request, classOfBusiness_id):
    return HttpResponse("You're looking at class of business %s." %classOfBusiness_id)

def results(request, classOfBusiness_id):
    response = "You're looking at the voting results of class of business %s."
    return HttpResponse(response % classOfBusiness_id)

def vote(request, classOfBusiness_id):
    return HttpResponse("You're voting on class of business %s." %classOfBusiness_id)
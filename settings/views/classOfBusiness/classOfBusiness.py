from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.contrib import messages

from settings.models import ClassOfBusiness
from settings.forms import classOfBusinessForm
from settings.models import ClassOfBusiness

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

# def deleteClassOfBusiness(request):
#     classToDelete = ClassOfBusiness.objects.all().values()
#     context={
#         "classToDelete": classToDelete
#     }

#     if request.method == "POST":
#         obj.delete()
#         return redirect("/settings/classOfBusiness")
    

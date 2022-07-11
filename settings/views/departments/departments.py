from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from settings.models import Department

def index(request):
    context = {'dataset': Department.objects.all()}
    return render(request, 'settings/departments/index.html', context)

def add(request):
    return render(request, "settings/departments/add.html")

def addRecord(request):
    x = request.POST['department']
    department = Department(department_text=x)
    department.save()
    return HttpResponseRedirect(reverse('department_index'))




    # def add(request):
    # context={}
    
    # form = classOfBusinessForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     messages.success(request, "Class of Business added successfully!")
    #     return HttpResponseRedirect(reverse('classOfBusiness_index'))

    # context['form'] = form
    # return render(request, "settings/classOfBusiness/add.html", context)

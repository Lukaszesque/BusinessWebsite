from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from settings.models import Department
from settings.services.shared.pagination.pagination import pagination

def index(request):
    context = {'dataset': pagination.get_page_obj(request, Department.objects.all().order_by('id'))}
    return render(request, 'settings/departments/index.html', context)

def add(request):
    return render(request, "settings/departments/add.html")

def addRecord(request):
    x = request.POST['department']
    department = Department(department_text=x)
    department.save()
    return HttpResponseRedirect(reverse('department_index'))

def delete(request, id):
    department_to_delete = Department.objects.get(id = id)
    department_to_delete.delete()
    return HttpResponseRedirect(reverse('department_index'))

def edit(request, id):
    department_to_edit = Department.objects.get(id = id)
    context = {
        'department_to_edit': department_to_edit,
    }
    return render(request, "settings/departments/edit.html", context)

def updateRecord(request, id):
    edited_record = request.POST['department']
    department_to_update = Department.objects.get(id = id)
    department_to_update.department_text = edited_record
    department_to_update.save()
    return HttpResponseRedirect(reverse('department_index'))
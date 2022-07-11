from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from settings.models import ClassOfBusiness
from settings.forms import classOfBusinessForm
from settings.services.shared.pagination.pagination import pagination


# To implement:
# Departments!

def index(request):

    return render(
        request, "settings/classOfBusiness/index.html", 
        context={
            'dataset': pagination.get_page_obj(request, ClassOfBusiness.objects.all().order_by('id'))
            })

def add(request):
    context={}
    
    form = classOfBusinessForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Class of Business added successfully!")
        return HttpResponseRedirect(reverse('classOfBusiness_index'))

    context['form'] = form
    return render(request, "settings/classOfBusiness/add.html", context)

def delete(request, id):
    classToDelete = ClassOfBusiness.objects.get(id=id)
    classToDelete.delete()
    return HttpResponseRedirect(reverse('classOfBusiness_index'))


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
    return HttpResponseRedirect(reverse('classOfBusiness_index'))

    

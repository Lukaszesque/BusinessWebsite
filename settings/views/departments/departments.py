from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'settings/departments/index.html', context)

def add(request):
    return render(request, "settings/departments/add.html")




    # def add(request):
    # context={}
    
    # form = classOfBusinessForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     messages.success(request, "Class of Business added successfully!")
    #     return HttpResponseRedirect(reverse('classOfBusiness_index'))

    # context['form'] = form
    # return render(request, "settings/classOfBusiness/add.html", context)

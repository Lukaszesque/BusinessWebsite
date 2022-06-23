from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'settings/departments/index.html', context)
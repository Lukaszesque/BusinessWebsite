from django.shortcuts import render

def index(request):
    context= {}
    return render(request, "settings/home/index.html", context)
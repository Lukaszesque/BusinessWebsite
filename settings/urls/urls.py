from django.urls import path, include, re_path
from settings.views.classOfBusiness import classOfBusiness
from settings import views

urlpatterns = [

    path('classOfBusiness/', include('settings.urls.ClassOfBusiness.urls')),
    path('departments/', include('settings.urls.Departments.urls')),

]
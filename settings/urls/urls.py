from django.urls import path, include, re_path
from settings.views.classOfBusiness import classOfBusiness
from settings import views

urlpatterns = [

    path('classOfBusiness/', include('settings.urls.ClassOfBusiness.urls')),




    #to repath:

    # ex: /settings/Departments - this should be moved elsewhere
    path('departments', views.index, name='settingsDepartments'),

    path('',  classOfBusiness.index, name='index'),
]
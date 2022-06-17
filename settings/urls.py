from django.urls import path
from .views.classOfBusiness import classOfBusiness
from settings import views

urlpatterns = [

    # ex: /
    path('',  classOfBusiness.index, name='index'),

    # ex: /settings/Departments
    path('settings/departments', views.settingsClassOfBusiness, name='settingsDepartments'),

    # ex: /settings/ClassOfBusiness
    path('settings/classOfBusiness', views.settingsClassOfBusiness, name='settingsClassOfBusiness'),

    path('settings/classOfBusiness/addNew', views.settingsAddNewClassOfBusiness, name='settingsClassOfBusinessAdd'),



]
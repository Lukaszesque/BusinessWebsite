from django.urls import path
from .viewsFolder.classOfBusiness import classOfBusiness
from settings import viewsFolder
from settings import views

urlpatterns = [

    # ex: /
    path('',  classOfBusiness.index, name='index'),

    # ex: /settings/Departments
    path('settings/departments', viewsFolder.settingsClassOfBusiness, name='settingsDepartments'),

    # ex: /settings/ClassOfBusiness
    path('settings/classOfBusiness', viewsFolder.settingsClassOfBusiness, name='settingsClassOfBusiness'),

    path('settings/classOfBusiness/addNew', viewsFolder.settingsAddNewClassOfBusiness, name='settingsClassOfBusinessAdd'),

    # ex: /settings/5
    path('settings/<int:classOfBusiness_id>/', views.detail, name='detail'),

    # ex /settings/5/results
    path('settings/<int:classOfBusiness_id>/results/', views.results, name='results'),

    # ex /settings/5/vote/
    path('settings/<int:classOfBusiness_id>/vote/', views.vote, name='vote')

]
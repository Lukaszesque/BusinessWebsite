from django.urls import path
from .views.classOfBusiness import classOfBusiness
from settings import views

urlpatterns = [

    path('',  classOfBusiness.index, name='index'),

    path('classOfBusiness/',  classOfBusiness.index, name='index'),

    path('classOfBusiness/delete/<int:id>', views.add, name='settingsClassOfBusinessDelete'),

    path('classOfBusiness/addNew', classOfBusiness.add, name='settingsClassOfBusinessAdd'),

    path('classOfBusiness/edit/<int:id>', views.edit, name='edit'),

    path('classOfBusiness/edit/updaterecord/<int:id>', views.updateRecord, name='updateRecord'),



    # ex: /settings/Departments - this should be moved elsewhere
    path('departments', views.index, name='settingsDepartments')
]
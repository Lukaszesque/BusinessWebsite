from django.urls import path
from settings.views.classOfBusiness import classOfBusiness

urlpatterns = [

    path('',  classOfBusiness.index, name='index'),

    path('delete/<int:id>', classOfBusiness.delete, name='delete'),

    path('addNew', classOfBusiness.add, name='add'),

    path('edit/<int:id>', classOfBusiness.edit, name='edit'),

    path('edit/updaterecord/<int:id>', classOfBusiness.updateRecord, name='updateRecord'),

]
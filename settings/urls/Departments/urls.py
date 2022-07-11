from django.urls import path
from settings.views.departments import departments

urlpatterns = [
    path('', departments.index, name='department_index'),
    path('add/', departments.add, name='add'),
    path('add/addrecord/', departments.addRecord, name='addRecord'),
    path('delete/<int:id>', departments.delete, name='delete'),
    path('edit/<int:id>', departments.edit, name='edit'),
    path('edit/updaterecord/<int:id>', departments.updateRecord, name='updaterecord')
]
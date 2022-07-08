from django.urls import path
from settings.views.departments import departments

urlpatterns = [
    path('', departments.index, name='index'),
    path('add/', departments.add, name='add')
]
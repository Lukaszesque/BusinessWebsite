from django.urls import path
from settings.views.departments import departments

urlpatterns = [
    path('', departments.index, name='index')
]
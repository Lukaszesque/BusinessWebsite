from django.urls import path

from settings import views

urlpatterns = [

    # ex: /
    path('', views.index, name='index'),

    # ex: /settings/Departments
    path('settings/departments', views.settingsDepartments, name='settingsDepartments'),

    # ex: /settings/ClassOfBusiness
    path('settings/classOfBusiness', views.settingsClassOfBusiness, name='settingsClassOfBusiness'),

    path('settings/classOfBusiness/addNew', views.settingsAddNewClassOfBusiness, name='settingsClassOfBusinessAdd'),

    # ex: /settings/5
    path('settings/<int:classOfBusiness_id>/', views.detail, name='detail'),

    # ex /settings/5/results
    path('settings/<int:classOfBusiness_id>/results/', views.results, name='results'),

    # ex /settings/5/vote/
    path('settings/<int:classOfBusiness_id>/vote/', views.vote, name='vote')

]
from django.urls import path

from settings import views

urlpatterns = [

    # ex: /
    path('', views.index, name='index'),

    # ex: /settings
    path('settings/', views.settingsIndex, name='settingsIndex'),

    # ex: /settings/5
    path('settings/<int:classOfBusiness_id>/', views.detail, name='detail'),

    # ex /settings/5/results
    path('settings/<int:classOfBusiness_id>/results/', views.results, name='results'),

    # ex /settings/5/vote/
    path('settings/<int:classOfBusiness_id>/vote/', views.vote, name='vote')

]
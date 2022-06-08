from django.urls import path

from settings import views

urlpatterns = [

    # ex: /fenfar/
    path('', views.index, name='index'),

    #ex: /fenfar/5
    path('<int:classOfBusiness_id>/', views.detail, name='detail'),

    #ex /fenfar/5/results
    path('<int:classOfBusiness_id>/results/', views.results, name='results'),

    #ex /fenfar/5/vote/
    path('<int:classOfBusiness_id>/vote/', views.vote, name='vote')

]
# pages/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('/despesas/', views.DespesasListView.as_view(), name='despesas'),
    path('/creater/', views.CreaterDespesasView.as_view(), name='creater-despesas'),
    path('r^delete/(?P<pk>\d+)/$', views.DeleteDespesasView.as_view(), name='delete-despesas'),
    path('/fitro_date/', views.filtroDespesasView.as_view(), name='fitro-date'),
    path('r^editer/(?P<pk>\d+)$', views.EditerDespesasView.as_view(), name='editer-despesas'),
    path('r^mais/(?P<pk>\d+)$', views.MaisDespesasView.as_view(), name='mais-despesas'),

]
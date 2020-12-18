from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('finance/', views.finance, name='finance'),
    path('data-analysis/', views.data_analysis, name='data_analysis')
]


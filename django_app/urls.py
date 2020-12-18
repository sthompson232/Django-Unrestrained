from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('test/', views.form_page, name='test'),
    path('finance/', views.finance, name='finance'),
    path('data-analysis/', views.data_analysis, name='data_analysis')
]


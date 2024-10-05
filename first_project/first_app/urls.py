from django.conf.urls import url
from first_app import views
from django.urls import  path

urlpatterns = [
    path('', views.index),
    #path('form_page/', views.form_name_view, name='form_name'),
    path('index/', views.index,name='index'),
   
]
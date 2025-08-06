from django.urls import path

from . import views 

app_name = 'clientes'  # << ESTE es el namespace


urlpatterns = [
    path('lista', views.lista, name='lista'), 
    path('nuevo/', views.nuevo_cliente, name='nuevo_cliente'),
]

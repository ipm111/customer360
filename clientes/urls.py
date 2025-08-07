from django.urls import path
from . import views 

app_name = 'clientes'  # << ESTE es el namespace



urlpatterns = [
    path('lista', views.lista, name='lista'), 
    path('nuevo/', views.nuevo_cliente, name='nuevo'),
    path('editar/<int:cliente_id>/', views.editar_cliente, name='editar'),
    path('eliminar/<int:cliente_id>/', views.eliminar_cliente, name='eliminar'),

]

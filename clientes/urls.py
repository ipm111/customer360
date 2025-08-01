from django.urls import path

from . import views 


urlpatterns = [
    path('', views.saludo, name='saludo'),    
    path('registrar/', views.registrar_cliente, name='registrar_cliente'),
    
]

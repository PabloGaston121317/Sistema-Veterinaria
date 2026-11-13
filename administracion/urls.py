from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('lista_clientes', views.lista_clientes, name= 'lista_clientes' ),
    path('lista_animales', views.lista_animales, name= 'lista_animales'),
    path('cliente/<int:num_dni>', views.cliente, name= 'cliente'),
    path('animal/<int:id>', views.animal, name= 'animal'),
    path('nuevo_animal2', views.nuevo_animal, name= 'nuevo_animal2'),
    path('nuevo_cliente', views.nuevo_cliente, name= 'nuevo_cliente'),
    path('modificar_animal/<int:pk>', views.modificar_animal, name='modificar_animal'),
    path('borrar_animal/<int:pk>', views.borrar_animal, name= 'borrar_animal'),
    path('modificiar_cliente/<int:pk>', views.modificar_cliente, name='modificar_cliente'),
    path('borrar_cliente/<int:pk>', views.borrar_cliente, name='borrar_cliente'),
]


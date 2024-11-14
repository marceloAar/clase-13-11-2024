from django.urls import path
from . import views

app_name = 'ofertas'

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_oferta/', views.crear_oferta, name='crear_oferta'),
    path('eliminar_oferta/<int:ofertas_id>/', views.eliminar_oferta, name='eliminar_oferta'),
    path('editar_oferta/<int:ofertas_id>/,', views.editar_oferta, name='editar_oferta'),
]

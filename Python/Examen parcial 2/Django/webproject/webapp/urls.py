from django.urls import path
from . import views

urlpatterns = [
    path('empresas/', views.empresa_index, name='empresa_index'),
    path('empleado/', views.empresa_index, name='empleado_index'),
    path('producto/', views.empresa_index, name='producto_index')
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('beneficiario', views.beneficiarios, name='beneficiarios'),
    path('beneficiario/crear', views.crearBeneficiario, name='crear'),
    path('beneficiario/editar', views.editarBeneficiario, name='editar'),
    path('eliminar/<int:id>/', views.eliminarBeneficiario, name="eliminar"),
    path('beneficiario/editar/<int:id>/', views.editarBeneficiario, name="editar")

]
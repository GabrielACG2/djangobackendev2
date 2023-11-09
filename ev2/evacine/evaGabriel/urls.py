"""
URL configuration for evaGabriel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from entrada import views as app1

app_name = 'entrada'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lista/', app1.listar_entradas, name='entrada-lista'),
    path('', app1.pagina_principal, name='pagina_principal'),
    path('crear/', app1.crear_entrada, name='entrada-crear'),
    path('editar/<int:id>/', app1.editar_entrada, name='entrada-actualizar'),
    path('borrar/<int:entrada_id>/', app1.eliminar_entrada, name='entrada-borrar'),
]




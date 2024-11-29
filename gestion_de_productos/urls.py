"""
URL configuration for gestion_de_productos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from gestion.views import *
from gestion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductoListView.as_view(),name='producto-list'),
    path('Nuevo-producto/',ProductoCreateView.as_view(),name='producto-create'),
    path('<int:pk>/editar/',ProductoUpdateView.as_view(),name='producto-edit'),
    path('<int:pk>/Eliminar-producto/', ProductoDeleteView.as_view(), name='producto-delete'),
    path('exportar-productos/', views.exportar_csv, name='exportar-csv'),
    ]

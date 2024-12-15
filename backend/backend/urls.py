"""
URL configuration for backend project.

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
from django.urls import path, include
from core.views import rastreabilidade
from core.views import gerar_relatorio_pdf, gerar_relatorio_xlsx
from rest_framework.routers import DefaultRouter
from core.views import UsuarioViewSet, MaterialViewSet
from . import views



router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'materiais', MaterialViewSet)

urlpatterns = [
    path('', views.home, name='home'),  # Adicionando uma rota para a raiz
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("api/rastreabilidade/", rastreabilidade, name="rastreabilidade"),
    path("api/relatorio/pdf/", gerar_relatorio_pdf, name="relatorio_pdf"),
    path("api/relatorio/xlsx/", gerar_relatorio_xlsx, name="relatorio_xlsx"),
    path('pesquisa/', views.pesquisa_material, name='pesquisa_material'),
]

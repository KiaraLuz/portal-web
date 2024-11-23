"""
URL configuration for portalweb project.

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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path('resena-historica/', views.resena_historica, name='resena_historica'),
    path('mision-vision/', views.mision_vision, name='mision_vision'),
    path('transparencias/', views.transparencias, name='transparencias'),
    path('resoluciones-actas-reglamentos/', views.resoluciones_actas_reglamentos, name='resoluciones_actas_reglamentos'),
    path('autoridades/', views.autoridades, name='autoridades'),
    path('escuela-profesional-de-ingenieria-de-sistemas/', views.sistemas, name='sistemas'),
    path('gestion-academica/', views.gestion_academica, name='gestion_academica'),
    path('programacion/', views.programacion, name='programacion'),
    path('gestion/', views.gestion, name='gestion'),
    path('ciberseguridad/', views.ciberseguridad, name='ciberseguridad'),
    path('bigdata/', views.bigdata, name='bigdata'),
    path('eventos/', views.eventos, name='eventos'),
]
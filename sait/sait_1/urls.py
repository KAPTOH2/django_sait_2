"""
URL configuration for sait_1 project.

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="h"),
    path("home/", views.home, name="home"),
    path("zadacha/<int:A>/<int:H>/<int:R>/<int:M>/", views.zadacha, name='zadacha'),
    path("razdel_1/", views.razdel_1, name="razdel_1"),
    path("massiv/", views.massiv, name="massiv"),
    path("student_grades/", views.student_grades, name="student_grades"),
    path('abc_model_form/', views.abc_model_form, name='abc_model_form'),
    path('abc_result/', views.abc_result, name='abc_result'),
    path('table/', views.table, name='table'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
]

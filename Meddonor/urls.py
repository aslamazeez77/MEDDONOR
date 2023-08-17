"""
URL configuration for Meddonor project.

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

from adminapp.views import adprocess
from guest.views import home, guestreg, ngoreg1, login1, ngoreg2, orpreg1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home),
    path('adprocess',adprocess),
    path('guestreg',guestreg),
    path('ngoreg1',ngoreg1),
    path('ngoreg2',ngoreg2),
    path('orpreg1',orpreg1),
    path('login1',login1)
]

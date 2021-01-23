"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from main_view.views import main_view , new_login
from menu.views import menuview, menu_response
from register.views import register, add_register
from device.views import device, add_device
from deviceqc.views import deviceqc_view, test_device
from salestype.views import salestype
from invoice.views import invoiceview
from create.views import create_view, create_new
from completeview.views import completeview_view, viewpage
from finalstock.views import finalstock_view, finalactions


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cognitive/', main_view, name='main'),
    path('cognitive/menu', menuview, name='menu'),
    path('menu_response/', menu_response),
    path('new_login/', new_login),
    path('cognitive/register', register, name='register'),
    path('add_register/', add_register),
    path('cognitive/device', device, name='device'),
    path('add_device/', add_device),
    path('cognitive/deviceqc', deviceqc_view, name='deviceqc'),
    path('test_device/', test_device),
    path('cognitive/finalstock', finalstock_view),
    path('finalactions/', finalactions),
    path('cognitive/salestype', salestype, name='salestype'),
    path('cognitive/invoice', invoiceview, name='invoiceview'),
    path('cognitive/create', create_view, name='create'),
    path('create_new/', create_new),
    path('cognitive/view', completeview_view),
    path('viewpage/', viewpage),
]

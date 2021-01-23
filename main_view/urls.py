from django.urls import path
from main_view import views

urlpatterns = [
    path('/cognitive', views.main_view, name='main_view')
]

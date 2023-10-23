from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('elements/', views.elements_view, name='elements'),
    path('create/excel/', views.get_excel, name='get_excel'),
]

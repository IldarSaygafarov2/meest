from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('elements/', views.elements_view, name='elements'),
    path('create/excel/', views.get_excel, name='get_excel'),
    path('save/<str:date_from>/<str:date_to>/', views.save_elements_by_datetime, name='save_excel')
]

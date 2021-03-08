from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
     # route for cats index
    path('records/', views.records_index, name='index')
]


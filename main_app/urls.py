from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('records/', views.records_index, name='index'),
    path('records/<int:record_id>', views.records_detail, name= 'detail'),
    path('records/<int:record_id>/add_played', views.add_played, name='add_played'),
    # associate a toy with a cat (M:M)
    path('records/<int:record_id>/assoc_cleaning_brush/<int:cleaning_brush_id>/', views.assoc_cleaning_brush, name='assoc_cleaning_brush'),
    path('records/<int:record_id>/remove_cleaning_brush/<int:cleaning_brush_id>/', views.remove_cleaning_brush, name='remove_cleaning_brush'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('records/', views.records_index, name='index'),
    path('records/<int:record_id>', views.records_detail, name= 'detail'),
    path('records/<int:record_id>/add_played/', views.add_played, name='add_played'),
    # associate a toy with a cat (M:M)
    path('records/<int:record_id>/assoc_cleaning_brush/<int:cleaning_brush_id>/', views.assoc_cleaning_brush, name='assoc_cleaning_brush'),
    path('records/<int:record_id>/remove_cleaning_brush/<int:cleaning_brush_id>/', views.remove_cleaning_brush, name='remove_cleaning_brush'),
    path('records/add_record/', views.add_record, name='add_record'),
    path('records/<int:record_id>/delete/', views.records_delete, name='delete'),
    path('records/<int:record_id>/edit/', views.records_edit, name='edit'),
    path('cleaning_equipment/add_product', views.add_cleaning_product, name='add_cleaning_product'),
    path('cleaning_equipment/', views.cleaning_equipment_index, name='cleaning_products'),
    path('cleaning_equipment/<int:equipment_id>/delete', views.cleaning_equipment_delete, name='delete_equipment')
]


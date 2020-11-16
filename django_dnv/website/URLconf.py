from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('emp/', views.emp, name='emp'),
    path('show/', views.show, name='show'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
]

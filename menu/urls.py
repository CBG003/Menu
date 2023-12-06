from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.show, name='listeM'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]

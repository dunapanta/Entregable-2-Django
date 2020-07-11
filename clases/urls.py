from django.urls import path
from clases import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:estudiante_id>/', views.estudiante, name='detail'),
    path('estudiantes', views.index, name='estudiantes'),
]

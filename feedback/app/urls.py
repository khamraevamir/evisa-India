from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('questions/', views.questions, name='questions'),
    path('success/', views.success, name='success'),
]
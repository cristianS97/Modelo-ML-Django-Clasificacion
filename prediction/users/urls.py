from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('check', views.CheckView.as_view(), name='check'),
    path('cierre/', views.logout, name='cierre')
]

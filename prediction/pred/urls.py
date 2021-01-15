from django.urls import path
from . import views

urlpatterns = [
    path('result/', views.ResultView.as_view(), name='result')
]

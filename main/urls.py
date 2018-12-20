from django.urls import path

from main import views

urlpatterns = [
    path('salam/', views.index, name='index')
]

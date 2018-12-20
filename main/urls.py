from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_single/<int:pk>', views.index_2, name='index_2'),
    path('<int:a>/<int:b>/', views.index_3, name='index_3'),
]

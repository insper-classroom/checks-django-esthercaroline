from django.urls import path

from . import views

urlpatterns = [
    path('creditos/', views.creditos, name='creditos'),
    path('', views.index, name='index'),]
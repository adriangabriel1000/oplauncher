from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.attendance_create, name='create'),
    path('', views.attendance, name='attendance'),
    path('list/', views.fullList, name='list'),

]
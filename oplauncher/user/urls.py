from django.views.generic import TemplateView
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', TemplateView.as_view(template_name='user/logout.html'), name='logout'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),

]
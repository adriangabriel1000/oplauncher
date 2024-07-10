from django.views.generic import TemplateView
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    #path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('password_change/', auth_view.PasswordChangeView.as_view(template_name='user/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_view.PasswordChangeDoneView.as_view(template_name='user/password_change_done.html'), name='password_change_done'),
    path('account_settings/', views.accSettings, name='accSettings'),
    path('register/', views.register, name='register'),
]
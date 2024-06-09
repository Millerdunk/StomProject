from django.urls import path
from . import views
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from .views import user_appointments
from .views import adm



urlpatterns = [
    path('home/', views.home, name='home'),
    path('serv/', views.serv, name='serv'),
    path('certificate/', views.certificate, name='certificate'),
    path('list_appointments/', views.list_appointments, name='list_appointments'),
    path('del_appointment/<int:patient_id>/', views.del_appointment, name='del_appointment'),
    path('adm/', views.adm, name='adm'),
    path('delete_appointment/', views.delete_appointment, name='delete_appointment'),
    path('footer/', views.footer, name='footer'),
    path('header/', views.header, name='header'),
    path('', views.index, name='index'),
    path('send_message/', views.send_message, name='send_message'),
    path('registr/', views.registr_view, name='registr'),
    path('acc/', views.acc, name='acc'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('user_appointments/', user_appointments, name='user_appointments'),
# ----------------------------сбр пар
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]




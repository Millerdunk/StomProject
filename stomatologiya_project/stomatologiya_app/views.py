from django.shortcuts import get_object_or_404, render, redirect
from stomatologiya_app.forms import ContactForm
from django.contrib import messages

# Отправка сообщения
def send_message(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            context = {
                'first_name': form.cleaned_data['first_name'],
                'message': form.cleaned_data['message'],
                'email': form.cleaned_data['email'],
                'phone_number': form.cleaned_data['phone_number'],
            }
            return render(request, 'acc.html', context)

        return redirect("acc")

    return render(request, "--", {"form": ContactForm()})

# Обработка формы
def form_view(request):
    if request.method == 'POST':
        return redirect('registr.html')
    return render(request, 'registr.html')

# Главная страница
def home(request):
    return render(request, 'home.html')

def serv(request):
    return render(request, 'serv.html')

def certificate(request):
    return render(request, 'certificate.html')

# Список записей
def list_appointments(request):
    return render(request, 'list_appointments.html')

# Страница индекса
def index(request):
    return render(request, 'index.html')

# Удаление записи
def delete_appointment(request):
    return render(request, 'delete_appointment.html')

# Страница администратора
def adm(request):
    return render(request, 'adm.html')

# Представление для регистрации
def registr_view(request):
    return render(request, 'registr.html')

# Страница аккаунта
def acc(request):
    return render(request, 'acc.html')

# Страница регистрации
def registration(request):
    return render(request, 'registration.html')

# Страница записей пользователя
def user_appointments(request):
    return render(request, 'user_appointments.html', {'user': request.user})

# Футер
def footer(request):
    return render(request, 'footer.html')

# Шапка
def header(request):
    return render(request, 'header.html')

# -------------------

from django import forms
from .models import Appointment

# Форма записи на прием
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'service', 'appointment_date']

# -------------------

from django.contrib.auth import login, authenticate
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from stomatologiya_app import models

# Регистрация пользователя
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            existing_user = models.CustomUser.objects.filter(email=email).exists()

            if existing_user:
                return render(request, 'register.html', {
                    'error': 'Такой пользователь уже существует',
                    'form': form
                })

            user = form.save()
            login(request, user)
            return redirect('user_appointments')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

# Вход пользователя
def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)
                
                if user.is_superuser:
                    return redirect('adm')
                else:
                    return redirect('user_appointments')
            else:
                messages.error(request, 'Неверные учетные данные')

    return render(request, 'login.html')

# -------------------

from django.shortcuts import render
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy

# Пользовательские представления для сброса пароля
def custom_password_reset(request):
    return PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html',
        success_url=reverse_lazy('password_reset_done')
    )(request)

def custom_password_reset_done(request):
    return PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    )(request)

def custom_password_reset_confirm(request, uidb64, token):
    return PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        success_url=reverse_lazy('password_reset_complete')
    )(request, uidb64=uidb64, token=token)

def custom_password_reset_complete(request):
    return PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    )(request)

# -------------------

from django.shortcuts import render
from .models import Appointment
from django.contrib.auth.decorators import login_required

# Записи пользователя (требуется аутентификация)
@login_required
def user_appointments(request):
    user = request.user
    appointments = Appointment.objects.filter(user=user)
    return render(request, 'user_appointments.html', {'appointments': appointments})

# -------------------

from .forms import AppointmentForm

# Создание записи на прием
def adm(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adm')

    else:
        form = AppointmentForm()

    return render(request, 'adm.html', {'form': form})

# -------------------

from django.shortcuts import render, redirect
from .forms import DeleteAppointmentForm

# Удаление записи
def delete_appointment(request):
    if request.method == 'POST':
        form = DeleteAppointmentForm(request.POST)
        if form.is_valid():
            appointments_to_delete = form.cleaned_data['appointments']
            appointments_to_delete.delete()
            return redirect('delete_appointment')
    else:
        form = DeleteAppointmentForm()

    return render(request, 'delete_appointment.html', {'form': form})

# -------------------

from .models import Patient
from django.utils import timezone

# Список всех записей
def list_appointments(request):
    appointments = Patient.objects.all()
    context = {'appointments': appointments}
    return render(request, 'list_appointments.html', context)

# Удаление записи по идентификатору
def del_appointment(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    patient.delete()
    return redirect('list_appointments')

# Обработка ответа на запись
def answer_appointment(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    
    # Обработка ответа на запись...
    
    # После ответа, установите флаг answered в True
    appointment.answered = True
    appointment.save()

    return redirect('list_appointments')

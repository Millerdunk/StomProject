from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager
from django.db import models
from datetime import datetime
from django.utils import timezone


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        # Создание обычного пользователя
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        # Создание суперпользователя
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = None

    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    answered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.email}"

    class Meta:
        ordering = ['-created_at']  # Сортировка по убыванию даты создания


class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, default=None)
    answered = models.BooleanField(default=False)

    class Meta:
        ordering = ['-user__date_joined']  # Сортировка по убыванию даты присоединения пользователя

    def __str__(self):
        return f" {self.patient} ваш доктор {self.doctor}, ваша запись назначена на {self.appointment_date.strftime('%d-%m-%Y %H:%M')}"

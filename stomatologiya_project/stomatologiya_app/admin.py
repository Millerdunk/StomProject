from django.contrib import admin
from .models import Patient, Service, Doctor, Appointment, CustomUser

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'message', 'email', 'phone_number')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'service', 'appointment_date')

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass
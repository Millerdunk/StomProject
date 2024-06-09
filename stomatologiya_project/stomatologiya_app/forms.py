from django import forms
from .models import Patient  # Подразумевается, что у вас есть модель patient


class ContactForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

# class LoginForm(forms.Form):
#     model = Patient
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)

# class RegistrationForm(forms.Form):
#     model = Patient
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)

# Регистрация-----------------

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser
from django import forms

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')  # Заменяем поле username на поле email

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')  # Указываем нужные поля для регистрации

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None  # Убираем дополнительный текст о требованиях к паролю

# ---------------------------------
    
from .models import Appointment

from .models import Appointment

class AppointmentForm(forms.ModelForm):
    
    user = forms.ModelChoiceField(
        queryset=CustomUser.objects.order_by('-date_joined'),  # Замените 'date_joined' на поле, по которому вы хотите сортировать
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,
    )

    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'service', 'appointment_date', 'user']  # Добавьте другие поля по мере необходимости
        


    appointment_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%d-%m-%YT%H:%M'],
    )
        
# -----------------------
from django import forms
from .models import Appointment

class DeleteAppointmentForm(forms.Form):
    appointments = forms.ModelMultipleChoiceField(
        queryset=Appointment.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
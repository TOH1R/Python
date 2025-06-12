from django import forms
from course.models import Register

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
            }),
            'site': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
            }),
        }

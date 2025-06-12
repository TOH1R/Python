from django import forms
from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__' 
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'style': 'border: 2px solid #007BFF; padding: 10px; width: 100%;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',  
                'style': 'border: 2px solid #007BFF; padding: 10px; width: 100%; margin-left: 70px;'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Message',
                'style': 'border: 2px solid #007BFF; padding: 10px; width: 470px;'
            }),
        }

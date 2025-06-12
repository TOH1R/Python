from django import forms
from Article.models import Contact, Comment, Email

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__' 
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter the subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your message', 
                'rows': 4
            }),
        }


class Contact2Form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
                'style': 'background-color: #212121; font-size: 15px; border: none; margin-top: 15px; width: 310px; color: darkgray;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'style': 'background-color: #212121; font-size: 15px; border: none; margin-top: 15px; width: 310px; color: darkgray;'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the subject',
                'style': 'background-color: #212121; font-size: 15px; border: none; margin-top: 15px; width: 310px; color: darkgray;'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your message',
                'rows': 4,
                'style': 'background-color: #212121; font-size: 15px; border: none; margin-top: 15px; width: 325px; color: darkgray;'
            }),
        }


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__' 
        widgets = {
           'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'style': 'border: 2px solid #007BFF; padding: 10px; width: 220px;'
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'  
        exclude = ('blog', )  
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'style': 'border: 2px solid #007BFF; padding: 10px; width: 100%;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
                'style': 'border: 2px solid #007BFF; padding: 10px; width: 100%;'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Message',
                'style': 'border: 2px solid #007BFF; padding: 10px; width: 100%; height: 150px;'
            }),
        }
        
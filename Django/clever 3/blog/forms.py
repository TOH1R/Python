from django import forms
from blog.models import Comment

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

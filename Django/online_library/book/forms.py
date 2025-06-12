from django import forms
from book.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"  # Include all fields
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'iamge': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            
        }

        
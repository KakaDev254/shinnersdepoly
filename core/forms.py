from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'role', 'message']
        labels = {
            'name': 'Your Name',
            'role': 'Your Role (e.g. Wedding Client)',
            'message': 'Your Message',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Birthday Client'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Share your experience', 'rows': 4}),
        }
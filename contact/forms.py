# contact/forms.py

from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'subject', 'message']
        labels = {
            'name': 'お名前',
            'email': 'メールアドレス',
            'subject': '件名',
            'message': '問い合わせ内容',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '山田 太郎', 'class': 'form-control' }),
            'email': forms.EmailInput(attrs={'placeholder': 'sample@example.com', 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': '件名', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'お問い合わせ内容をご記入ください', 'class': 'form-control'}),
    }

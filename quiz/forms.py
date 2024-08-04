from django import forms
from .models import Question

# 管理画面用のフォーム
class QuestionAdminForm(forms.ModelForm):
    
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
from django.db import models

# Create your models here.

# クイズのジャンルモデル
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# 問題の難易度モデル
class Difficulty(models.Model):
    level = models.CharField(max_length=10)
    
    def __str__(self):
        return self.level

# 問題モデル
class Question(models.Model):
    INPUT_TYPE_CHOICES = [
        ('choice', 'Multiple Choice'),
        ('text', 'Text Input'),
    ]
    
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    difficulty = models.ForeignKey('Difficulty', on_delete=models.CASCADE)
    # 問題文
    text = models.CharField(max_length=500)
    # 選択肢
    option1 = models.CharField(max_length=100, blank=True, default='')
    option2 = models.CharField(max_length=100, blank=True, default='')
    option3 = models.CharField(max_length=100, blank=True, default='')
    option4 = models.CharField(max_length=100, blank=True, default='')
    # 正解
    correct_answer = models.CharField(max_length=100)
    # 回答方法。デフォルトは４択
    input_type = models.CharField(max_length=10, choices=INPUT_TYPE_CHOICES, default='choice')
    
    def __str__(self):
        return self.text
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
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    difficulty = models.ForeignKey('Difficulty', on_delete=models.CASCADE)
    # 問題文
    text = models.CharField(max_length=500)
    # 選択肢
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    # 正解
    correct_answer = models.CharField(max_length=100)
    
    def __str__(self):
        return self.text
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('select_difficulty/<int:category_id>', views.select_difficulty, name='select_difficulty'),
    path('quiz/<int:category_id>/<int:difficulty_id>/', views.quiz, name='quiz'),
    path('question/<int:question_id>/', views.question, name='question'),
    path('check_answer/<int:question_id>/', views.check_answer, name='check_answer'),
    path('result', views.result, name='result'),
]
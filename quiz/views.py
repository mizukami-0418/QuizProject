from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Difficulty, Question

# Create your views here.

def home(request):
    # ホーム画面でジャンル選択
    category = Category.objects.all()
    difficulty = Difficulty.objects.all()
    return render(request, 'home.html', {'categories': category, 'difficulties': difficulty})


def quiz(request, category_id, difficulty_id):
    # 指定されたカテゴリと難易度に一致する問題をランダムに10問取得
    questions = Question.objects.filter(category_id=category_id, difficulty_id=difficulty_id).order_by('?')[:10]
    # 取得した問題のIDをリストとしてセッションに保存します。
    request.session['questions'] = [question.id for question in questions]
    # 現在の問題のインデックスをセッションに保存します。最初は0に設定します。
    request.session['current_question'] = 0
    # 現在のスコアをセッションに保存します。初期スコアは0に設定します。
    request.session['score'] = 0
    # 最初の問題のページにリダイレクトします。
    return redirect('question', question_id=questions[0].id)


def question(request, question_id):
    # quizで取得した問題10問をquestionに格納
    question = get_object_or_404(Question, id=question_id)
    # questionを保持してquestion.htmlを描画
    return render(request, 'quiz/question.html', {'question': question})
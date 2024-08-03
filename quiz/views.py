from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Difficulty, Question

# Create your views here.

def home(request):
    # ホーム画面でジャンル選択
    category = Category.objects.all()
    return render(request, 'home.html', {'categories': category})

def select_difficulty(request, category_id):
    # 難易度を選択
    difficulty = Difficulty.objects.all()
    # 選んだカテゴリーをCategoryから取得
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'quiz/select_difficulty.html', {'difficulties': difficulty, 'category': category})

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


def check_answer(request, question_id):
    # DBから問題を取得
    question = get_object_or_404(Question, id=question_id)
    # 挑戦者の回答を取得
    selected_option = request.POST.get('option')
    # 回答が正解か確認
    is_correct = selected_option == question.correct_answer
    
    if is_correct:
        request.session['score'] += 1 # 正解だった場合はスコアを1増やす
    
    request.session['current_question'] += 1 # 問題数を１増やし次に進む
    
    # 出題数が9問以下なら次の問題へ進む
    if request.session['current_question'] < 10:
        # 次の問題のIDを取得
        next_question_id = request.session['questions'][request.session['current_question']]
        # 次の問題を描画
        return render(request, 'quiz/answer.html', {'question': question, 'is_correct': is_correct, 'next_question_id': next_question_id})
    
    else:
        question_number = request.session['current_question']
        return render(request, 'quiz/answer.html', {'is_correct': is_correct, 'question_number': question_number})
    # else: # 10問以上になったらresultへリダイレクト
    #     return redirect('result')

# 結果の表示
def result(request):
    score = request.session.get('score', 0)
    return render(request, 'quiz/result.html', {'score': score})

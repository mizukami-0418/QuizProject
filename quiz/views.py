from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Difficulty, Question
import unicodedata
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
    # questionsリストのindexが「0」のidを引数にして、questionにリダイレクト。
    return redirect('question', question_id=questions[0].id)


def question(request, question_id):
    # quizで取得した問題10問からidが「0」の問題をquestionに格納
    question = get_object_or_404(Question, id=question_id)
    # カテゴリーのタイトルを取得
    category_name = question.category.name
    # 難易度を取得
    difficulty_level = question.difficulty.level
    # questionを保持してquestion.htmlを描画
    return render(request, 'quiz/question.html', {'question': question, 'category_name': category_name, 'difficulty_level': difficulty_level})


def normalize_answer(answer):
    """入力された回答を正規化する関数。前後の空白を取り除き、全角を半角に変換する。"""
    if answer is None:
        return ""
    # 前後の空白を取り除き、全角文字を半角文字に正規化
    return unicodedata.normalize('NFKC', answer.strip())


def check_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id) # DBから問題を取得
    # 回答方法により、正誤の判定を分岐
    if question.input_type == 'text': # テキスト入力の場合
        selected_option = request.POST.get('answer') # テキスト入力の回答を取得
        is_correct = normalize_answer(selected_option) == normalize_answer(question.correct_answer) # 正規化された回答を解答と照合
    else:
        selected_option = request.POST.get('option') # 選択肢の回答を取得
        # 回答の正誤を判定
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
        return render(request, 'quiz/answer.html', {'question': question,'is_correct': is_correct, 'question_number': question_number})
    # else: # 10問以上になったらresultへリダイレクト
    #     return redirect('result')

# 結果の表示
def result(request):
    score = request.session.get('score', 0)
    return render(request, 'quiz/result.html', {'score': score})

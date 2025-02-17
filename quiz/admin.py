from django.contrib import admin
from .models import Category, Difficulty, Question
from .forms import QuestionAdminForm
# Register your models here.

# カテゴリーモデルのカスタマイズ
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'easy_questions', 'normal_questions', 'hard_questions', 'extra_hard_questions')
    # EASYの問題数
    def easy_questions(self, obj):
        return Question.objects.filter(category=obj, difficulty__level='EASY').count()
    easy_questions.short_description = '初級の問題数'
    # NORMALの問題数
    def normal_questions(self, obj):
        return Question.objects.filter(category=obj, difficulty__level='NORMAL').count()
    normal_questions.short_description = '中級の問題数'
    # HARDの問題数
    def hard_questions(self, obj):
        return Question.objects.filter(category=obj, difficulty__level='HARD').count()
    hard_questions.short_description = '上級の問題数'
    # EXTRA HARDの問題数
    def extra_hard_questions(self, obj):
        return Question.objects.filter(category=obj, difficulty__level='EXTRA HARD').count()
    extra_hard_questions.short_description = 'エキスパートの問題数'

# 問題モデルのカスタマイズ
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'category', 'difficulty', 'input_type')
    list_filter = ('category', 'difficulty', 'input_type')
    search_fields = ('text',)
    form = QuestionAdminForm

admin.site.register(Category, CategoryAdmin)
admin.site.register(Difficulty)
admin.site.register(Question, QuestionAdmin)
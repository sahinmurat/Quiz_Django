from django.contrib import admin
import nested_admin
from .models import Category, Question,Quiz,Answer

class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    
    
class QuestinInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerInline]    

class QuizAdmin(nested_admin.NestedModelAdmin):
    model = Quiz
    inlines = [QuestinInline]
    



admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Answer)

# Register your models here.

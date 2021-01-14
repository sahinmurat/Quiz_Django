from django.contrib import admin
from .models import Category, Question,Quiz,Answer

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Answer)

# Register your models here.

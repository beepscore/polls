from django.contrib import admin
from polls.models import Question


class QuestionAdmin(admin.ModelAdmin):
    # list publication date, then question text
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)

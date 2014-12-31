from django.contrib import admin
from polls.models import Question


class QuestionAdmin(admin.ModelAdmin):
    # use fieldsets to show title
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]


admin.site.register(Question, QuestionAdmin)

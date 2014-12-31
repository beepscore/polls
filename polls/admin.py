from django.contrib import admin
from polls.models import Choice, Question


class QuestionAdmin(admin.ModelAdmin):
    # use fieldsets to show title
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

from django.contrib import admin
from . models import Question, Subquestion, Questionnaire


admin.site.register(Question)
admin.site.register(Subquestion)
admin.site.register(Questionnaire)
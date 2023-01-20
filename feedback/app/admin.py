from django.contrib import admin
from .models import Question, Subquestion, Questionnaire
from django.conf.locale.es import formats as es_formats

es_formats.DATETIME_FORMAT = "d M Y H:i:s"
admin.site.register(Question)
admin.site.register(Subquestion)


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
        def format_date(self, obj):
                return obj.date.strftime("%d %b %Y %H:%M:%S")
        list_display = (
                    "last_name",
                    "first_name",
                    'passport_no',
                    'marital_status',
                    'format_date'
                    )




from django.contrib import admin
from .models import Question,Choice
# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0
class QuestionAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Question',               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines =[ChoiceInline]
    search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)




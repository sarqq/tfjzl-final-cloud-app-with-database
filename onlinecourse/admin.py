"""
Django app development w/SQL and databases - Final Project

Task 2: Import models and register model changes
"""

from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# Task 2: QuestionInline class
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

# Task 2: ChoiceInline class
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Task 2: QuestionAdmin class
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ["content"]

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
# Task 2: register Question, Choice and Submission models
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
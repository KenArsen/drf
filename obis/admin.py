from django.contrib import admin
from obis.models import Lesson, Student


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_number', 'name')
    search_fields = ('lesson_number', 'name')
    list_filter = ('lesson_number', 'name')
    list_display_links = ('lesson_number',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_number', 'name', 'surname')
    search_fields = ('student_number', 'name', 'surname')
    list_filter = ('student_number', 'name', 'surname')
    list_display_links = ('student_number',)

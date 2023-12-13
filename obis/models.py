from django.db import models


class Lesson(models.Model):
    lesson_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.lesson_number} - {self.name}'


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    student_number = models.CharField(max_length=10, unique=True)
    course = models.PositiveSmallIntegerField(default=1)
    lessons = models.ManyToManyField(Lesson, related_name='lessons', blank=True)

    def __str__(self):
        return f'{self.name} - {self.surname}'

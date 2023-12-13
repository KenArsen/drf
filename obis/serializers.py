from rest_framework import serializers

from .models import Lesson, Student


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    # lessons = serializers.HyperlinkedRelatedField(many=True, view_name='lesson-detail', read_only=True)
    lessons = serializers.StringRelatedField(many=True)

    class Meta:
        model = Student
        fields = ('id', 'name', 'surname', 'student_number', 'course', 'lessons')

from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student-list'),
    path('lessons/', views.lesson_list, name='lesson-list'),
    path('students/create/', views.student_create, name='student-create'),
    path('lessons/create/', views.lesson_create, name='lesson_create'),
    path('students/<int:pk>/', views.student_detail, name='student-detail'),
    path('lessons/<int:pk>/', views.lesson_detail, name='lesson-detail'),
    path('students/<int:pk>/update/', views.student_update, name='student-update'),
    path('lessons/<int:pk>/update/', views.lesson_update, name='lesson-update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student-delete'),
    path('lessons/<int:pk>/delete/', views.lesson_delete, name='lesson-delete'),
]

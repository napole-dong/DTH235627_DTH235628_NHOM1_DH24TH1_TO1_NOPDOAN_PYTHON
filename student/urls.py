from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.student_list, name='student_list'),
    path("add/", views.add_student, name="add_student"),
    path('students/<slug:slug>/', views.view_student, name='view_student'),
    path('edit/<slug:slug>/', views.edit_student, name='edit_student'),
    path('delete/<slug:slug>/', views.delete_student, name='delete_student'),

]
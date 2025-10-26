from django.contrib import admin
from .models import Teacher

# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_ID', 'first_name', 'last_name', 'department', 'subject', 'mobile_number', 'email')
    list_filter = ('department', 'gender', 'joining_date')
    search_fields = ('teacher_ID', 'first_name', 'last_name', 'email', 'mobile_number')
    prepopulated_fields = {'slug': ('first_name', 'last_name', 'teacher_ID')}

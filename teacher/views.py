from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Teacher
from django.contrib import messages

# Create your views here.
def teacher_list(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers
    }
    return render(request, "teachers/teachers.html", context)

def add_teacher(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        teacher_ID = request.POST.get('teacher_ID')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')
        department = request.POST.get('department')
        subject = request.POST.get('subject')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')
        teacher_image = request.FILES.get('teacher_image')
        
        teacher = Teacher.objects.create(
            first_name=first_name,
            last_name=last_name,
            teacher_ID=teacher_ID,
            date_of_birth=date_of_birth,
            gender=gender,
            qualification=qualification,
            experience=experience,
            department=department,
            subject=subject,
            joining_date=joining_date,
            mobile_number=mobile_number,
            email=email,
            present_address=present_address,
            permanent_address=permanent_address,
            teacher_image=teacher_image
        )
        
        messages.success(request, "Teacher added successfully.")
        return redirect('teacher_list')
    
    return render(request, "teachers/add-teacher.html")

def view_teacher(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    context = {
        'teacher': teacher
    }
    return render(request, "teachers/teacher-details.html", context)

def edit_teacher(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    
    if request.method == "POST":
        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.teacher_ID = request.POST.get('teacher_ID')
        teacher.date_of_birth = request.POST.get('date_of_birth')
        teacher.gender = request.POST.get('gender')
        teacher.qualification = request.POST.get('qualification')
        teacher.experience = request.POST.get('experience')
        teacher.department = request.POST.get('department')
        teacher.subject = request.POST.get('subject')
        teacher.joining_date = request.POST.get('joining_date')
        teacher.mobile_number = request.POST.get('mobile_number')
        teacher.email = request.POST.get('email')
        teacher.present_address = request.POST.get('present_address')
        teacher.permanent_address = request.POST.get('permanent_address')
        
        if request.FILES.get('teacher_image'):
            teacher.teacher_image = request.FILES.get('teacher_image')
        
        teacher.save()
        messages.success(request, "Teacher updated successfully.")
        return redirect('teacher_list')
    
    return render(request, "teachers/edit-teacher.html", {'teacher': teacher})

def delete_teacher(request, slug):
    if request.method == "POST":
        teacher = get_object_or_404(Teacher, slug=slug)
        teacher_name = f"{teacher.first_name} {teacher.last_name}"
        teacher.delete()
        messages.success(request, f"Teacher {teacher_name} deleted successfully.")
        return redirect('teacher_list')
    return HttpResponseForbidden()

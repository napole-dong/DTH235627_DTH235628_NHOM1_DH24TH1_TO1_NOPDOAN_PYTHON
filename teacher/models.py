from django.db import models
from django.utils.text import slugify

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    teacher_ID = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')])
    qualification = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    joining_date = models.DateField()
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    present_address = models.TextField()
    permanent_address = models.TextField()
    teacher_image = models.ImageField(upload_to='teacher_images/', blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}-{self.teacher_ID}")
        super(Teacher, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.teacher_ID})"

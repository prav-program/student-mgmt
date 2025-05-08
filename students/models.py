from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=255)
    student_class = models.CharField(max_length=50)
    admission_date = models.DateField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_name
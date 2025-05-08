from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

@login_required
def student_list(request):
    query = request.GET.get('q', '')
    students = Student.objects.filter(is_deleted=False)
    if query:
        students = students.filter(Q(student_name__icontains=query) | Q(student_class__icontains=query))

    paginator = Paginator(students, 5)
    page = request.GET.get('page')
    students = paginator.get_page(page)
    return render(request, 'students/student_list.html', {'students': students, 'query': query})

@login_required
def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/student_form.html', {'form': form})

@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/student_form.html', {'form': form})

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.is_deleted = True
    student.save()
    return redirect('student_list')

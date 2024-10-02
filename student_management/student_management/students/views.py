from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def student_list(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(
            models.Q(first_name__icontains=query) |
            models.Q(last_name__icontains=query)
        )
    else:
       students_list = Student.objects.all()
    paginator = Paginator(students_list, 10)  # Show 10 students per page

    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)
    return render(request, 'students/student_list.html', {'students': students, 'query': query})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

@login_required
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})
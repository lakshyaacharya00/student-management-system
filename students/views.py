# from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Student
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages

@login_required
def home(request):

    search = request.GET.get('search')

    if search:
        students = Student.objects.filter(
            Q(name__icontains=search) |
            Q(branch__icontains=search)
        )
    else:
        students = Student.objects.all()

    total_students = Student.objects.count()

    return render(request, 'home.html', {
        'students': students,
        'total_students': total_students
    })


from django.shortcuts import render
from .models import Student

@login_required
def add_student(request):

    if request.method == "POST":

        name = request.POST.get('name')
        age = request.POST.get('age')
        branch = request.POST.get('branch')

        Student.objects.create(
            name=name,
            age=age,
            branch=branch
        )
        messages.success(request, "Student added successfully!")


        return render(request, 'add_student.html', {
        })

    return render(request, 'add_student.html')

@login_required
def edit_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.branch = request.POST.get('branch')

        student.save()

        return redirect('home')
    messages.success(request, "Student updated successfully!")

    return render(request, 'edit_student.html', {
        'student': student
    })

@login_required
def delete_student(student,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('home')

@login_required
def student_detail(request, id):

    student = Student.objects.get(id=id)

    return render(request, 'student_detail.html', {
        'student': student
    })
# Create your views here.
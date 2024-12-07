from django.shortcuts import render, redirect
from .models import Student


def student_list(request):
    students = Student.objects.all()
    ctx = {'students': students }
    return render(request, 'students/student-list.html', ctx)


def student_create(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    age = request.POST.get('age')
    email = request.POST.get('email')

    if first_name and last_name and age and email :
        Student.objects.all(
            first_name=first_name,
            last_name=last_name,
            age=age,
            email=email
        )
        return redirect('students:list')

    return render(request, 'students/student-form.html')





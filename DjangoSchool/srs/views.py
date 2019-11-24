# Create your views here.
from django.shortcuts import render, redirect

from srs.models import College, Student, Teacher


def index(request):
    return render(request, 'index.html', {
        'colleges': College.objects.all()
    })


def show_college_detail(request):
    try:
        collid = int(request.GET.get('collid', '0'))
        college = College.objects.filter(id=collid).first()
        if college:
            students = Student.objects.filter(college=collid)
            teachers = Teacher.objects.filter(college=collid)
            return render(request, 'detail.html', {
                'college': college,
                'students': students,
                'teachers': teachers
            })
    except ValueError:
        pass
    return redirect('/')
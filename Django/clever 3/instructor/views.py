from django.shortcuts import render
from instructor.models import Teachers, Best_teacher

def instructors(request):
    student = Teachers.objects.all()
    best_teacher = Best_teacher.objects.all()  
    
    context = {
        'student': student,
        'best_teacher': best_teacher
    }      

    
    return render(request, 'instructors.html', context=context)
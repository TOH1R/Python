from django.shortcuts import render, get_object_or_404
from course.models import Course, Event
from course.forms import RegisterForm
from course.models import Course
from blog.models import Blog
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    courses = Course.objects.all()[:3]
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            
    events = Event.objects.all()   
    blogs = Blog.objects.all()
     
            
    context = {
        'courses': courses,
        'form': form,
        'events': events,
        'blogs': blogs
    }
    return render(request, 'index.html', context=context)

def courses(request):
    courses = Course.objects.all()[:8]
    
    
    context = {
        'courses': courses
    }

    return render(request, 'courses.html', context=context)

def index_login(request):
    courses = Course.objects.all()[:3]
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
         
    events = Event.objects.all()   
    blogs = Blog.objects.all()     
            
            
    context = {
        'courses': courses,
        'events': events,
        'form': form,
        'blogs': blogs
        
    }

    return render(request, 'index-login.html', context=context)


def search(request):
    search = request.GET.get("search")
    courses = Course.objects.filter(title__icontains=search)
    

    context = {
        'courses': courses ,
        'search': search   
        }
    return render(request, template_name='search.html', context=context)

def detail(request, pk):
    course = get_object_or_404(Course.objects.all(), id=pk)
    category = course.category
    three_coursee = Course.objects.filter(category=category)
    context = {
        'course': course,
        'three_coursee': three_coursee
    }
    return render(request, 'single-course.html', context=context)




def regular_page(request):  
    return render(request, 'regular-page.html')


def From_detail(request):
    return render(request, 'detail.html')
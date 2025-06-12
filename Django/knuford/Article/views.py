from django.shortcuts import render, redirect, get_object_or_404
from Article.models import Blog, Category, Work, Student
from Article.forms import ContactForm,Contact2Form
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from Article.forms import ContactForm, CommentForm, EmailForm
from django.contrib.auth.models import User


def index(request):
    blogs = Blog.objects.all()        
    category = Category.objects.all()
    work = Work.objects.all()
    students = Student.objects.all()
    users = User.objects.count()

    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            
    context = {
        'form': form,
        'blogs': blogs,
        'category': category,
        'work': work,
        'students': students,
        'users': users
        
    }
    return render(request, 'index.html', context=context)

def blog_single(request, pk):
    blog = get_object_or_404(Blog.objects.all(), id=pk)
    work = Work.objects.all()
    
    
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.blog = blog
            obj.save()
      
    email = EmailForm()
    if request.method == "POST":
        form = EmailForm(data=request.POST)
        if form.is_valid():
            form.save()     
               
    context = {
        'form': form,
        'blog': blog,
        'email': email,
        'work': work,
        
    }
    
            
    return render(request, 'blog-single.html', context=context)

def contact(request):
   
    form = Contact2Form()
    if request.method == "POST":
        print(request.POST)
        form = Contact2Form(data=request.POST)
        if form.is_valid():  
            form.save()      
            
    context = {
        'form': form
    }
    return render(request, 'contact.html', context=context)



def register_function(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form
    }        
    
    return render(request, 'registere.html', context=context)
      
           
def login_function(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    context = {
        'form': form
    }        
    
    return render(request, template_name='login.html', context=context)

def logout_function(request):
    logout(request)
    return redirect('login')        
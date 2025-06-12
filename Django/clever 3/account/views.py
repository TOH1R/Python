from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


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
    
    return render(request, 'register.html', context=context)
      
           
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
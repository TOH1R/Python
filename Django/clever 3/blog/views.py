from django.shortcuts import render, get_object_or_404
from blog.models import Blog, Category
from blog.forms import CommentForm

def blog(request):
    blogs = Blog.objects.all()        
    category = Category.objects.all()
    context = {
        'blogs': blogs,
        'category': category
    }

    return render(request, 'blog.html', context=context)

def blog_detail(request, pk):
    blog = get_object_or_404(Blog.objects.all(), id=pk)
    blogs = Blog.objects.all()[:2] 
    category = Blog.category 
    
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.blog = blog
            obj.save()
          
    context = {
        'blogs': blogs,
        'category': category,
        'blog': blog,
        'form': form
    }
    return render(request, 'blog-details.html', context=context)

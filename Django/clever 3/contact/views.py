from django.shortcuts import render
from contact.forms import ContactForm

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            
            
    context = {
        'form': form
    }
    return render(request, 'contact.html', context=context)


def blog_details(request):
    return render(request, 'blog-details.html')
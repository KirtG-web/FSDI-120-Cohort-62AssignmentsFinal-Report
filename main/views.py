from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

# NOTE: The set_language view is removed because you are now 
# using the built-in Django i18n URL include.

def home(request):
    return render(request, 'index.html') # Ensure this matches your filename

def erzsebet(request):
    return render(request, 'erzsebet.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def resources(request):
    return render(request, 'resources.html')

def clothing(request):
    return render(request, 'clothing.html')

def food(request):
    return render(request, 'food.html')

def holidays(request):
    return render(request, 'holidays.html')

def history(request):
    return render(request, 'history.html')

def language(request):
    return render(request, 'language.html')

def landmarks(request):
    return render(request, 'landmarks.html')

def culture(request):
    return render(request, 'culture.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        
        send_mail(
            subject="New Contact Form Message",
            message=full_message,
            from_email=email,
            recipient_list=['kirtdgerman13f@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, "Message sent successfully!")
        return redirect('contact')
    return render(request, 'contact.html')

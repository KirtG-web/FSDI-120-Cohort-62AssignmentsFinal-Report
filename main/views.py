from django.shortcuts import render
from django.shortcuts import redirect 
from django.http import HttpResponse

def set_language(request):
    if request.method == 'POST':
        lang = request.POST.get('language')
        request.session['language'] = lang
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def home(request):
    return render(request, 'index.html')

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

def landmarks(request):
    return render(request, 'landmarks.html')

def contact(request):
    return render(request, 'contact.html')

def history(request):
    return render(request, 'history.html')

def language(request):
    return render(request, 'language.html')

def culture(request):
    return render(request, 'culture.html')

from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # TEMP: simple check
        if username == 'admin' and password == '1234':
            return HttpResponse("Login successful!")
        else:
            return HttpResponse("Invalid credentials", status=401)

    return render(request, 'login.html')
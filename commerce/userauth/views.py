from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from .forms import UserRegisterForm
from .models import User

UserAuth = settings.AUTH_USER_MODEL

def register_view(request):

    if request.user.is_authenticated:
        messages.success(request, f"You have been logged in")
        return redirect("store:index")
    
    if request.method == 'POST':
        form    = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data['username']
            messages.success(request, f"Hi {username}, Your account was been created successfully")
            new_user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, new_user)
            print(form.cleaned_data['password1'])
            return redirect("store:index")
    else:
        form    = UserRegisterForm()

    context = {
        'form': form,
    }
    
    return render(request, 'page/auth/sign-up.html', context)
        

def login_view(request):
    context = {'error': False}
    
    if request.user.is_authenticated:
        messages.success(request, f"You have been logged in")
        return redirect("store:index")
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            context['error'] = True
            context['error_messages'] = ["Email does not exist"]
            messages.warning(request, f"Email does not exist")
            return render(request, 'userauth/sign-in.html', context)
    
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You are Signed in.")
            print(messages)
            return redirect("store:index")
            
        else:
            context['error'] = True
            context['error_messages'] = ["Invalid Password"]
            messages.warning(request, f"Password Does not match")
            
    return render(request, 'page/auth/sign-in.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, "Signed out")
    return redirect("userauth:sign-in")
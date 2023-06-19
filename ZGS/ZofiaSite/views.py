from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Mess
from .forms import MessForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string
from django.utils.translation import gettext as _
from django.utils.translation import activate, LANGUAGE_SESSION_KEY


def home(request):
    if request.user.is_authenticated:
        form = MessForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                m = form.save(commit=False)
                m.user = request.user
                m.save()
                messages.success(request, ("Post utworzony pomyślnie :)"))
                return redirect('home')
        mess = Mess.objects.all().order_by("-created_at")
        return render(request, 'home.html', {"mess":mess, "form":form})
    else:
        mess = Mess.objects.all().order_by("-created_at")
        return render(request, 'home.html', {"mess":mess})

def home_en(request):
    if request.user.is_authenticated:
        form = MessForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                m = form.save(commit=False)
                m.user = request.user
                m.save()
                messages.success(request, ("Post was made :)"))
                return redirect('home_en')
        mess = Mess.objects.all().order_by("-created_at")
        return render(request, 'home_en.html', {"mess":mess, "form":form})
    else:
        mess = Mess.objects.all().order_by("-created_at")
        return render(request, 'home_en.html', {"mess":mess})
    

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        html = render_to_string('profile_list.html', {'profiles': profiles})
        return HttpResponse(html)
    else:
        return HttpResponse('Musisz być zalogowany, aby zobaczyć co tu się dzieje :D', status=401)

def profile_list_en(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        html = render_to_string('profile_list_en.html', {'profiles': profiles})
        return HttpResponse(html)
    else:
        return HttpResponse('You need to be logged in to see what is here :D', status=401)
        
def gallery(request):
    html = render_to_string('gallery.html')
    return HttpResponse(html)

def gallery_en(request):
    html = render_to_string('gallery_en.html')
    return HttpResponse(html)

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        mess = Mess.objects.filter(user_id=pk)
        if request.method == "POST":
            current_user_profile = request.user.profile
            action = request.POST['follow']
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            elif action == "follow":
                current_user_profile.follows.add(profile)
            current_user_profile.save()
        return render(request, "profile.html", {"profile":profile, "mess":mess})
    else:
        messages.success(request, ("Musisz byc zalogowany aby tu wejsc"))
        return redirect('home')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Zalogowano pomyślnie :D"))
            return redirect('home')
        else:
            messages.success(request, ("Nie udało się zalogować :("))
            return redirect('login')
    else:
        return render(request, "login.html", {})
    
def login_user_en(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You are logged in :D"))
            return redirect('home_en')
        else:
            messages.success(request, ("Oh no, wrong data :("))
            return redirect('login_en')
    else:
        return render(request, "login_en.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Wylogowano pomyslnie, do zobaczenia! <3"))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Konto stowrzone! ;)"))
            return redirect('home')
    return render(request, "register.html", {'form':form})

def register_user_en(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Welcome to teh flower shop! ;)"))
            return redirect('home_en')
    return render(request, "register_en.html", {'form':form})

def set_language(request):
    language_code = request.GET.get('language_code')
    if language_code:
        request.session[LANGUAGE_SESSION_KEY] = language_code
        activate(language_code)
    return redirect('home')
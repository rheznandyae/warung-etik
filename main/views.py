from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm


def home(request):
    return render(request, 'main/home.html')

def loginUser(request):
    nextUrl = request.GET.get('next', '')
    if request.user.is_authenticated:
        if nextUrl == '':
            return redirect('../') # isi stringnya dengan url dashboard
    else:
        if request.method == 'POST':
            nextUrl = request.POST.get('next', '')
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if request.user.is_superuser:
                    return redirect('/dashboard/')
                if nextUrl == "":
                    return redirect('../') # isi stringnya dengan url dashboard
                return redirect(nextUrl) # isi string nya dengan next
            else:
                messages.info(request, 'Username or password is incorrect')
        response = {}
        return render(request, 'main/login.html', response)
    

def register(request):
    if request.user.is_authenticated:
        return redirect('../') # isi stringnya dengan url dashboard
    else:
        form = CreateUserForm()
        
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your account was successfully created")
                return redirect('/login/')
        response = {'form' : form, 'errors': form.errors.values()}
        return render(request, 'main/register.html', response)
    

def search(request):
    return render(request, 'main/search.html')

def logoutUser(request):
    logout(request)
    return redirect('/login/')

            



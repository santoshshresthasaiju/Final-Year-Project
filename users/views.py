from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
@login_required(login_url="login")
def homepage(request):

    return render(request, 'users/index.html')

def register_view(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        initial_data = {'username':'', 'email':'', 'password1':'','password2':''}
        form = CreateUserForm(initial=initial_data)
    context = {'registerform':form}

    return render(request, 'users/register.html', context=context)


@login_required(login_url="login")
def dashboard_view(request):
    

    return render(request, 'users/dashboard.html')

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)

                return redirect('home')
            
    context = {'loginform':form}

    return render(request, 'users/login.html', context=context)

@login_required(login_url='login')
def logout_view(request):
    auth.logout(request)
    return redirect("login")
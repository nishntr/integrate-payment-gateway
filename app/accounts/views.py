from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('payment:checkout')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('payment:checkout')

    return render(request, 'login_register.html', {'page': page})


def logoutUser(request):
    logout(request)
    return redirect('accounts:login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.user.is_authenticated:
        return redirect('payment:checkout')
    if request.method == 'POST':
        print("register")
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.save()
            print(user)
            # if user is not None:
            login(request, user)
            return redirect('payment:checkout')

    context = {'form': form, 'page': page}
    return render(request, 'login_register.html', context)

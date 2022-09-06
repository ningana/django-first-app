from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . forms import LoginForm, SignupForm


def logout_page(request):
    logout(request)
    return redirect('login')


def login_page(request):
    form = LoginForm()
    message = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = "Invalide Authentication"
    return render(request, "authentication/login.html", context={'form':form, 'message':message})


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # Enregistrement dans la base de donnée
            login(request, user)  # On connecte user
            """
            Le fait d'avoir importer settings nous permetait s'acceder
            au paramettre généreaux"""
            return redirect('signuped', form.cleaned_data['username'])
    return render(
        request, "authentication/signup.html", context={'form':form}
    )


def signuped(request, username):
    """
    Cette est fonction est utilisé pour rediriger user apres son inscription à mon site web
    """
    return render(request, "authentication/singuped.html", context={"username":username})
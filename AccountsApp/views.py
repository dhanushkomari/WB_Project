from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
# LOGIN VIEW..................................................................
def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('App:home')
        else:
            return HttpResponse("wrong creds entered")
    else:
        return render(request, 'AccountsApp/login.html')
#...............................................................................




@login_required
def LogoutView(request):
    logout(request)
    return redirect('AccountsApp:login')    
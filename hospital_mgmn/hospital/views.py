from django.shortcuts import redirect ,render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import CreateUserForm
from django.contrib import messages

def About(request):
    return render(request, 'about.html')

def Home(request):
    return render(request, 'home.html')

def Contact(request):
    return render(request, 'contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'index.html')

# def Login(request):
#     error = ""
#     if request.method == "POST":
#         u = request.POST['uname']
#         p = request.POST['pwd']
#         user = authenticate(username = u, password = p)
#         try:
#             if user.is_staff:
#                 login(request,user)
#                 error = "no"
#             else:
#                 error = "yes"
#
#         except:
#             error = "yes"
#     d = {'error':error}
#     return render(request,'login.html', d)
#
# def Logout_admin(request):
#     if not request.user.is_staff:
#         return redirect('Logout_admin')
#     logout(request)
#     return redirect('admin_login')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                messages.success(request, 'Account was created for ' + first_name + ' ' + last_name)

                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)
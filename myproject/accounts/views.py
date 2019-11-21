from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from . import forms
# Create your views here.

def index(request):
    shelf = User.objects.all()
    return render(request, 'accounts/list_users.html',{'shelf': shelf})

def UpdateUser(request,id):
    user_update = User.objects.get(id=id)

    data = {
        'username' : user_update.username,
        'email'    : user_update.email,
        # 'password1': user_update.password,
        # 'password2': ,
    }

    form = forms.UpdateUserForm(request.POST or None, instance=user_update)
    if request.method == "POST":  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/accounts/users/list')  
            except:  
                pass 
            return HttpResponse(form.save())

    context = {
        "page_title" : "Edit User",
        "form"       : form,
        "users"      : user_update,
    }
    return render(request,'accounts/add_edit.html',context) 

def DeleteUser(request, id):
    user_id = int(id)
    try:
        user = User.objects.get(id = id)
    except User.DoesNotExist:
        return redirect('users_list')
    user.delete()
    return redirect('users_list')

def AddUser(request):  
    form = forms.AddUserForm(request.POST or None)
    if request.method == "POST":  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/accounts/users/list')  
            except:  
                pass
    context = {
        "page_title" : "Add User",
        "form"       : form,
    }
    return render(request,'accounts/add_edit.html',context)


def SignUp(request):
    if request.method == 'POST':
        form = forms.AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/accounts/login/')
    else:
        form = forms.AddUserForm()
    return render(request, 'auth/signup.html', {'form': form})


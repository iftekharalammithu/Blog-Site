from tokenize import group
from unicodedata import name
from django.shortcuts import render, HttpResponseRedirect
from .models import post1
from .forms import loginform, signupform , postForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
# Create your views here.

def home(request):
    posts = post1.objects.all()
    return render(request, 'blog/home.html', {'post':posts})

def about(request):
    return render (request, 'blog/about.html')

def contract(request):
    return render (request, 'blog/contract.html')
    
def deshboard(request):
    if request.user.is_authenticated:
        posts = post1.objects.all()
        full_name = request.user.get_full_name()
        gp = request.user.groups.all()
        return render (request, 'blog/deshboard.html', {'post':posts, 'full_name':full_name, 'groups1': gp})
    else:
        return HttpResponseRedirect('/login/')
    
def addpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = postForm(request.POST)
            if form.is_valid():
                form.save()
                form = postForm()
                messages.success(request, 'Post Submit SuccessFully')
        else:
            form = postForm()
        return render (request,'blog/addpost.html', {'form': form})
    else:
     return HttpResponseRedirect ('/login/')

def deletepost(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = post1.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/deshboard/')
    else:
     return HttpResponseRedirect ('/login/')

def updatepost(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = post1.objects.get(pk=id)
            form = postForm(request.POST, instance=pi) 
            if form.is_valid():
             form.save()
        else:
            pi = post1.objects.get(pk=id)
            form = postForm(instance=pi) 
        return render(request, 'blog/updatepost.html', {'ff':form})
    else:
        return HttpResponseRedirect('/login/')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = loginform(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login Sucessfull')
                    return HttpResponseRedirect ('/deshboard/')
        else:
            form = loginform()
        return render (request, 'blog/login.html', {'loginfm': form})
    else:
        return HttpResponseRedirect ('/deshboard/')


def user_signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Create SuccessFully')
            user = form.save()
            group = Group.objects.get(name='author')
            user.groups.add(group)
    else:
        form = signupform()
    return render (request, 'blog/signup.html', {'fm':form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect ('/')

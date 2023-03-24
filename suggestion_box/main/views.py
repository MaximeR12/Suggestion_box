from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from main.models import Idea, IdeaCreationForm

def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'homepage.html', {'user':request.user})
    else:
        return render(request, 'homepage.html')

def ideas(request):
    if not request.user.is_authenticated: #if the user is not authenticated
        messages.success(request, "Please login before booking an appointment")
        return redirect('login') #redirect to login page

    else:
        your_ideas = []
        other_ideas = []
        for idea in Idea.objects.all():
            if idea.author == request.user:
                your_ideas.append(idea)
            else:
                other_ideas.append(idea)
        if request.method == 'POST':
            form = IdeaCreationForm(request.POST)
            if form.is_valid():
                idea = form.cleaned_data['name']
                details = form.cleaned_data['details']
                new_idea = Idea(
                name = idea,
                details = details,
                )
                new_idea.author = request.user
                new_idea.save()
                messages.success(request, 'Idée ajoutée à la liste')
                return redirect('ideas')
            else:
                messages.success(request, "Il y a eu un probème avec votre idée, réessayez")
        else:
            form = IdeaCreationForm()        
            return render(request, 'ideas.html', {'form':form, 'your_ideas': your_ideas, 'other_ideas':other_ideas})

def new_idea(request):
    if not request.user.is_authenticated: #if the user is not authenticated
        messages.success(request, "Please login before booking an appointment")
        return redirect() #redirect to login page

    else:
        if request.method == 'POST':
            form = IdeaCreationForm(request.POST)
            if form.is_valid():
                idea = form.cleaned_data['name']
                details = form.cleaned_data['details']
                new_idea = Idea(
                name = idea,
                details = details,
                )
                new_idea.author = request.user
                new_idea.save()
                messages.success(request, 'Idée ajoutée à la liste')
                return redirect('homepage')
        form = IdeaCreationForm()        
        return render(request, 'new_idea.html', {'form':form})

def delete_idea(request,id):
    idea = Idea.objects.get(id = id)
    idea.delete()
    return redirect('ideas')

def add_like(request, id):
    idea = Idea.objects.get(id = id)
    idea.likes += 1
    idea.save()
    return redirect('ideas')


def register_user2(request):
    return render(request, "register.html")

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, "Account created, you're now logged in")
            return redirect('homepage')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {
        "form" : form,
        })

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print("POST")
        if user is not None:
            print("USER")
            login(request, user)
            messages.success(request, "You're now logged in")
            return redirect('ideas')
        else:
            messages.success(request, "Could not log you in, verify your username/password")
            return redirect('login')

    else:
        return render(request, 'login.html') 

def logout_user(request):
    logout(request)
    messages.success(request, "Succesfully Logged out !")
    return redirect('homepage')
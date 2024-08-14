from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

def home(request):
    return render (request , 'home.html')

def registration(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request , "Username Already Taken Please Choose Another")
            return redirect('/register/')
        
        user = User.objects.filter(email = email)
        if user.exists():
            messages.info(request , "This Email-Id is already Registered.")
            return redirect('/register/')
        
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email = email
        )
        user.set_password(password)
        user.save()
        messages.success(request , "Account Created Successfully!!!")
        return redirect('/register/')
        
    return render(request , 'register.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username = username).exists():
            messages.warning(request , "Invalid Username")
            return redirect('/login/')
        
        user = authenticate(username = username , password = password)
        if user is None:
            messages.warning(request , "Invalid Password")
            return redirect('/login/')
        
        else:
            login(request , user)
            return redirect('/receipes/')
            
    return render(request , 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url = "/login/")
def receipes(request):
    queryset = Receipe.objects.all()
    
    # icontains is use to search thhe given word in receipe 
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
    
    paginator = Paginator(queryset , 5)
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
        
    context = {'queryset' : page_obj}
    return render (request , 'receipes.html' , context)


def see_receipe(request , id):
    queryset = Receipe.objects.filter(id = id)
    context = {'queryset' : queryset}
    return render (request , 'receipe_detail.html',context)

@login_required(login_url = "/login/")
def add_receipe(request):
    if request.method == "POST":
        data = request.POST
        
        user = request.user
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_ingredients = data.get('receipe_ingredients')
        
        Receipe.objects.create(
            user = user,
            receipe_image=receipe_image,
            receipe_name = receipe_name,
            receipe_description = receipe_description ,
            receipe_ingredients = receipe_ingredients ,
        )
        return redirect('/receipes/')
        
    return render (request , 'add_receipe.html')

@login_required(login_url = "/login/")
def update_receipe(request , id):
    queryset = Receipe.objects.get(id = id)
    
    if request.method == "POST":
        data = request.POST
        
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        
        if receipe_image :
            queryset.receipe_image = receipe_image
            
        queryset.save()
        return redirect('/receipes/')
    context = {'receipe' : queryset}
    return render (request ,'update_receipe.html' , context)
    
@login_required(login_url = "/login/")
def delete_receipe(request , id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes/')

def about_us(request):
    return render(request, 'about.html')

# def feedback(request):
#     return render(request, 'feedback.html')
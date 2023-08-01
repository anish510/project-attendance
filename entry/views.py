from django.shortcuts import render,redirect
from django.http import HttpResponse
from entry.models import *
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user =  User.objects.filter(email_address = email,password = password)
        if user.exists():
            return render(request,'home.html', {'user':user})
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('login')
        
        
 
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        phonenumber = request.POST.get('phonenumber')
        address = request.POST.get('address')
        role = request.POST.get('role')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
                user =  User.objects.filter(email_address = email)
                if  user.exists():
                    messages.error(request,"Account already exist")
                    return redirect('register')
            
                else:
                    user = User.objects.create(
                    password = password,
                    first_name = firstname,
                    last_name = lastname,
                    gender_field = gender,
                    date_of_birth= dob,
                    phone_number = phonenumber,
                    email_address = email,
                    address = address,
                    role = role)
                    user.save()
                    return render(request,'login.html')
        else:
            messages.error(request,"Password does not match")
            return redirect('register')
            
    return render(request,'register.html')

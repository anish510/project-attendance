from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from entry.models import *
from django.contrib import messages
from django.contrib.auth import logout
# from django.contrib.auth.decorators import login_required






# Create your views here.
def home(request):
    user =  User.objects.all()
    # print(3232323232323)
    # user = request.session.get('user_id')
    # print(777777777777777777,user) 
    return render(request,'home.html',{'user':user})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user =  User.objects.filter(email_address = email,password = password)
        if user.exists():
            user=user.first()
            print(22222222222,user.id)
            request.session['user_id'] = user.id
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

def logout_out(request):
    if 'user_id' in request.session:
        del request.session['user_id']  # Delete the user_id from the session
    return redirect('login')


def punch(request):
    if request.method == "POST":
        
        
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User,id = user_id)
        
        date = request.POST.get('date')
        punchin = request.POST.get('punchInTime')
        punchout = request.POST.get('punchOutTime')
        breakin = request.POST.get('breakInTime')
        breakout = request.POST.get('breakOutTime')
        print(999999999999999,user)
        
        
        
        attendance = Attendance.objects.create(
            user =user,
            punch_in = punchin,
            punch_out = punchout,
            break_in = breakin,
            break_out = breakout,
            date = date,
            )
        attendance.save()
        messages.success(request,"Successful")
        return render(request,'home.html', {'user':user})   
    else:
        messages.error(request,"Unsuccessful")
        return render(request,'home.html')
                                               
        
      

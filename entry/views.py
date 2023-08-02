from django.shortcuts import render,redirect,get_object_or_404
from entry.models import *
from django.contrib import messages
from datetime import datetime,timedelta
from django .contrib.auth.hashers import make_password ,check_password
# from django.contrib.auth.decorators import login_required






# Create your views here.
def home(request):
    user =  User.objects.all()
    return render(request,'home.html',{'user':user})
    
def login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        
        user =  User.objects.filter(email_address = email)
        if user.exists():
            user=user.first()
            if check_password(password,user.password):
                
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
                    hashed_password = make_password(password)
                    user = User.objects.create(
                    password = hashed_password,
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
        select_category = request.POST.get('category')
        print(333333333333333333,select_category)
        
        date = request.POST.get('date')
        time_str = request.POST.get('time')
        time_obj = datetime.strptime(time_str, '%H:%M').time()


        attendance, created = Attendance.objects.get_or_create(user=user, date=date)

        if select_category == 'punch_in':
            attendance.punch_in = time_obj
        elif select_category == 'break_in':
            attendance.break_in = time_obj
        elif select_category == 'break_out':
            attendance.break_out = time_obj
        elif select_category == 'punch_out':
            attendance.punch_out = time_obj
            
        attendance.save()
        messages.success(request,"Successful")
        return render(request,'home.html', {'user':user})   
    else:
        messages.error(request,"Unsuccessful")
        return render(request,'home.html')
    

    
def recordsheet(request,user_id):
    if request.method == "POST":
        user = get_object_or_404(User,pk = user_id)
        date = request.POST.get('date')
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        
        
        
       
            
        attendance_records  = Attendance.objects.filter(user = user, date = input_date)
        
        
        total_work_hours = 0
        for attendance in attendance_records:
            if attendance.punch_in and attendance.punch_out:
                punch_in_time = datetime.combine(attendance.date, attendance.punch_in)
                punch_out_time = datetime.combine(attendance.date, attendance.punch_out)
                
                time_difference = punch_out_time - punch_in_time
                total_work_hours += time_difference.total_seconds() / 3600
        
        
        
        return render(request,'recordsheet.html',{'attendance':attendance_records , 'user':user,'date':date,'total_work_hours': total_work_hours})
    else:
        messages.error(request,"Unsuccessful")
        return render(request,'recordsheet.html')
    
    
    
    
      

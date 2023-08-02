from django.db import models
from common.enums import GENDER_CHOICE,ROLE_CHOICES
# from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.
# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("The Email field must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=50,unique = True)
    password = models.CharField(max_length=20)
    gender_field = models.CharField(max_length=20 , choices= GENDER_CHOICE)
    date_of_birth = models.DateField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices= ROLE_CHOICES)
    
    # USERNAME_FIELD = 'email_address'
    # REQUIRED_FIELDS = ['first_name', 'last_name', 'gender_field', 'date_of_birth', 'phone_number', 'address', 'role']


    # objects = CustomUserManager()
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    # def set_role(self, role):
    #     if role in dict(self.ROLE_CHOICES).keys():  # Check if the given role is a valid choice
    #         self.role = role
    #     else:
    #         raise ValueError("Invalid role")

    # def get_role_display(self):
    #     return dict(self.ROLE_CHOICES).get(self.role, "")  # Get the display value for the role

    
class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
    date = models.DateField()
    punch_in = models.TimeField(null = True)
    punch_out = models.TimeField(null = True)
    break_in = models.TimeField(null = True)
    break_out = models.TimeField(null = True)
    
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' ' + str(self.date)
    
    # @property
    # def total_work(self):
    #     from datetime import datetime
    #     if self.punch_in and self.punch_out:
    #         punch_in_time = datetime.combine(self.date, self.punch_in)
    #         punch_out_time = datetime.combine(self.date, self.punch_out)
    #         time_difference = punch_out_time - punch_in_time
    #         total_hours = time_difference.total_seconds() / 3600
    #         return round(total_hours, 2)
    #     return 0  # If either punch_in or p
    
    

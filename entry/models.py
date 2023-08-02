from django.db import models
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=50,unique = True)
    password = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=50)
   
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
    date = models.DateField()
    punch_in = models.TimeField(null = True)
    punch_out = models.TimeField(null = True)
    break_in = models.TimeField(null = True)
    break_out = models.TimeField(null = True)
    
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' ' + str(self.date)
    

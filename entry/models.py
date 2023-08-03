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
    
    
class Timesheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    def worked_hr(self):
        total = 0
        punch_in_entry = None
        punch_out_entry = None

        entries = self.timesheetentries_set.all()
        punch_in_entry = entries.filter(entry_type='punch_in').first()
        punch_out_entry = entries.filter(entry_type='punch_out').first()
        print(punch_in_entry ,punch_out_entry,'---------------')

        if punch_in_entry and punch_out_entry:
            time_difference = punch_out_entry.entry_time - punch_in_entry.entry_time
            total = time_difference.total_seconds()/3600

        return total
                
    
CHOICES = (
    ('punch_in','punch_in'),
    ('punch_out','punch_out'),
    ('break_in','break_in'),
    ('break_out','break_out'),
)
class TimesheetEntries(models.Model):
    timesheet = models.ForeignKey(Timesheet, on_delete=models.CASCADE)
    entry_type = models.CharField(choices=CHOICES, max_length= 30)
    entry_time = models.DateTimeField()
  
    
    


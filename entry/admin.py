from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email_address')
    
@admin.register(models.Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user','date','punch_in','punch_out','break_in','break_out')
    
@admin.register(models.Timesheet)
class TimesheetAdmin(admin.ModelAdmin):
    list_display = ('user','date')
    
@admin.register(models.TimesheetEntries)
class TimesheetEntriesAdmin(admin.ModelAdmin):
    list_display = ('entry_type','entry_time')

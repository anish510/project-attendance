from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User),
admin.site.register(models.Attendance),
admin.site.register(models.Timesheet),
admin.site.register(models.TimesheetEntries),

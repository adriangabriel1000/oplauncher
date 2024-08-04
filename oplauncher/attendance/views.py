from django.shortcuts import render
from .forms import AttendanceForm
from .models import Attendance
from django.contrib.auth.decorators import login_required
from datetime import datetime
#from django.utils import timezone


# Create your views here.
@login_required
def attendance_create(request):
    if request.method=='POST':
        form = AttendanceForm(data=request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
    else:
        form = AttendanceForm(data=request.GET)
    return render(request, 'attendance/create.html', {
        'form': form,
    })


@login_required
def attendance(request):
    #stDt = timezone.now().time()
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    hour = datetime.now().hour + 2
    minute = datetime.now().minute
    
    if datetime(year, month, day, hour, minute) > datetime(year, month, day , 7, 0) and datetime(year, month, day, hour, minute) < datetime(year, month, day, 15, 0):
        stTme = datetime(year, month, day , 7, 0)
        enTme = datetime(year, month, day, 15, 0)
    
    if datetime(year, month, day, hour, minute) > datetime(year, month, day , 15, 0) and datetime(year, month, day, hour, minute) < datetime(year, month, day, 23, 0):
        stTme = datetime(year, month, day , 15, 0)
        enTme = datetime(year, month, day, 23, 0)
    
    if datetime(year, month, day, hour, minute) > datetime(year, month, day , 23, 0) and datetime(year, month, day+1, hour, minute) < datetime(year, month, day+1, 7, 0):
        stTme = datetime(year, month, day , 23, 0)
        enTme = datetime(year, month, day+1, 7, 0)
    
    attendance = Attendance.objects.filter(startTime__gte=stTme, endTime__lte=enTme)
    #print(year, month, day, hour, minute)
    return render(request, 'attendance/attendance.html', {
        'attendance': attendance,
    })
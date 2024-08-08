from django.shortcuts import render, redirect
from .forms import AttendanceForm
from .models import Attendance
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils import timezone


# Create your views here.
@login_required
def attendance_create(request):
    if request.method=='POST':
        form = AttendanceForm(data=request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
    
    form = AttendanceForm(data=request.GET)
    return render(request, 'attendance/create.html', {
        'form': form,
    })


@login_required
def attendance(request):
    #stDt = timezone.now().time()
    day = timezone.now().day
    month = timezone.now().month
    year = timezone.now().year
    hour = timezone.now().hour + 2
    minute = timezone.now().minute
    handle = "Not Set"
    
    if datetime(year, month, day, hour, minute) > datetime(year, month, day , 7, 0) and datetime(year, month, day, hour, minute) < datetime(year, month, day, 15, 0):
        stTme = datetime(year, month, day , 7, 0)
        enTme = datetime(year, month, day, 15, 0)
        handle = "Morning Shift"
    
    if datetime(year, month, day, hour, minute) > datetime(year, month, day , 15, 0) and datetime(year, month, day, hour, minute) < datetime(year, month, day, 23, 0):
        stTme = datetime(year, month, day , 15, 0)
        enTme = datetime(year, month, day, 23, 0)
        handle = "Afternoon Shift"
    
    if datetime(year, month, day, hour, minute) > datetime(year, month, day , 23, 0) and datetime(year, month, day, hour, minute) < datetime(year, month, day, 23, 59):
        stTme = datetime(year, month, day , 23, 0)
        enTme = datetime(year, month, day+1, 7, 0)
        handle = "Night Shift before 12"
        
    if datetime(year, month, day, hour, minute) > datetime(year, month, day , 0, 0) and datetime(year, month, day, hour, minute) < datetime(year, month, day, 7, 0):
        stTme = datetime(year, month, day-1 , 23, 0)
        enTme = datetime(year, month, day, 7, 0)
        handle = "Night Shift after 12"
    
    attendance = Attendance.objects.filter(startTime__gte=stTme, startTime__lte=enTme)
    print(year, month, day, hour, minute)
    print(datetime(2024, 8, 5, 15, 5,))
    print(handle)
    return render(request, 'attendance/attendance.html', {
        'attendance': attendance,
    })
    
@login_required
def fullList(request):
    list = Attendance.objects.all()
    return render(request, 'attendance/list.html', {
        'list': list,
    })
    
@login_required
def delete(request, id):
    if request.method == 'POST':
        attendance = Attendance.objects.get(id=id)
        attendance.delete()
    return redirect('list')
        
        
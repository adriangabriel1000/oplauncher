from django.shortcuts import render
from .forms import AttendanceForm
from django.contrib.auth.decorators import login_required

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

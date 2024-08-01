from .models import Attendance
from django import forms

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ('user', 'startTime', 'endTime', 'position', 'location')


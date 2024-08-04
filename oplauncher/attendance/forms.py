from .models import Attendance
from django import forms


class DateInput(forms.DateInput):
    input_type = 'datetime-local'


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ('user', 'startTime', 'endTime', 'position', 'location')
        widgets={
            'startTime': DateInput(),
            'endTime': DateInput(),      
        }


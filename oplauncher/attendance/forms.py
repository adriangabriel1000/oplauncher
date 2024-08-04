from .models import Attendance
from django import forms


class AttendanceForm(forms.ModelForm):
    
    pos = (
        ("XM", "XM"),
        ("XA", "XA"),
        ("XN", "XN"),
        ("XD", "XD"),
        ("XZ", "XZ"),
    )
    
    position = forms.ChoiceField(choices=pos, widget=forms.RadioSelect())
    
    class Meta:
        model = Attendance
        fields = ('startTime', 'endTime', 'position', 'location')
        widgets={
            'startTime': forms.DateInput(attrs={'type': 'datetime-local'}),
            'endTime': forms.DateInput(attrs={'type': 'datetime-local'}),
            

            
        }


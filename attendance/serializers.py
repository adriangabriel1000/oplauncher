from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    
    def getUsername(self, obj):
        return obj.user.username
    
    def getFirstName(self, obj):
        return obj.user.first_name
    
    def getLastName(self, obj):
        return obj.user.last_name

    username = serializers.SerializerMethodField("getUsername")
    firstName = serializers.SerializerMethodField("getFirstName")
    lastName = serializers.SerializerMethodField("getLastName")
    
    
    class Meta:
        model = Attendance
        fields = ('user', 'username', 'firstName', 'lastName', 'startTime', 'endTime', 'position', 'location')

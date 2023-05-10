from rest_framework import serializers
from datetime import date

from APP_TODO.models import Task

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['title']
    def validate(self, data):
        today = date.today()
        if data['date'] < today:
            raise serializers.ValidationError("this date canot be added")
        
        return data
        
class ToDoSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['title']

   
        
    
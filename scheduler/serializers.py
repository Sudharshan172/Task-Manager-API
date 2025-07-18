# scheduler/serializers.py
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_status(self, new_status):
        instance = self.instance
        valid_transitions = {
            'pending': ['running', 'failed'],
            'running': ['completed', 'failed'],
            'completed': [],
            'failed': [],
        }

        if instance:
            current_status = instance.status
            if new_status != current_status and new_status not in valid_transitions[current_status]:
                raise serializers.ValidationError(
                    f"Invalid status transition from '{current_status}' to '{new_status}'"
                )
        return new_status

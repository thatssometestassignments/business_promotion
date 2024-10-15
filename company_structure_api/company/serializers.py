from rest_framework import serializers
from .models import Department, Employee


class DepartmentSerializer(serializers.ModelSerializer):
    employee_count = serializers.IntegerField(read_only=True)
    total_salary = serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2)

    class Meta:
        model = Department
        fields = ['id', 'name', 'employee_count', 'total_salary']


class EmployeeSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 'full_name', 'photo', 'position', 'salary', 'age', 'department']

    def get_full_name(self, obj):
        if obj.last_name:
            return f"{obj.first_name} {obj.last_name}"
        return obj.first_name

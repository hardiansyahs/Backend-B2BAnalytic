# api <-> mobile app/ web app/etc. json

from rest_framework import serializers
from .models import Employee
from .models import Account


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        # or you can use field = ('id'. 'fullname', 'emp_code', 'mobile')


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

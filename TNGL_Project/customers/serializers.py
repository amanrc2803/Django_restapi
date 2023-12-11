from rest_framework import serializers
from .models import Customer




class CustomerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Customer
        fields = (
                'cus_id',
                  'name',
                  'address',
                  'customer_number',
                  'meter_serial_number'
                )
from rest_framework import serializers
from rest_framework import viewsets
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ['id', 'name', 'surname', 'login', 
                    'password', 'email', 
                  'role', 'date_of_add', 'phone']



class RoleSerializer(serializers.ModelSerializer):
    class Meta():
        model = Role
        fields = ['id', 'name']



class StatusSerializer(serializers.ModelSerializer):
    class Meta():
        model = Status
        fields = ['id', 'name']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'orderNumber', 'status', 'waiter', 'table',
                    'is_it_open', 'order_date']


class TableSerializer(serializers.ModelSerializer):
    class Meta():
        model = Table
        fields = ['id', 'name']

    
class MealSerializer(serializers.ModelSerializer):
    class Meta():
        model = Meal
        fields = ['id', 'name', 'price', 'description', 'category']


class MealCategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = MealCategory
        fields = ['id', 'name', 'department']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta():
        model = Department
        fields = ['id', 'name']


class CheckModelSerializer(serializers.ModelSerializer):
    class Meta():
        model = CheckModel
        fields = ['id', 'order',  
                  'orderedMeals', 'date', 'service_percentage', 'service_fee', 'total_sum']

class ServicePercentageSerializer(serializers.ModelSerializer):
    class Meta():
        model = ServicePercentage
        fields = ['id', 'percentage']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta():
        model = OrderItem
        fields = ['id', 'order', 'meal', 'mealCount']

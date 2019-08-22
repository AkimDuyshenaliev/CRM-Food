from rest_framework import serializers
from rest_framework import viewsets
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ['name', 'surname', 'login', 
                    'password', 'email', 
                  'role', 'date_of_add', 'phone']



class RoleSerializer(serializers.ModelSerializer):
    class Meta():
        model = Role
        fields = ['name']


class UsertokenSerializer(serializers.ModelSerializer):
    pass


class StatusSerializer(serializers.ModelSerializer):
    class Meta():
        model = Status
        fields = ['name']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'status', 'waiter', 'table',
                    'is_it_open', 'order_date']


class TableSerializer(serializers.ModelSerializer):
    class Meta():
        model = Table
        fields = ['name']

    
class MealSerializer(serializers.ModelSerializer):
    class Meta():
        model = Meal
        fields = ['name', 'price', 'description', 'category']


class MealCategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = MealCategory
        fields = ['name', 'department']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta():
        model = Department
        fields = ['name']


class CheckModelSerializer(serializers.ModelSerializer):
    class Meta():
        model = CheckModel
        fields = ['date', 'service_fee', 'total_sum', 
                  'meals', 'service_percentage']

class ServicePercentageSerializer(serializers.ModelSerializer):
    class Meta():
        model = ServicePercentage
        fields = ['percentage']


# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     @action(methods=['delete'], detail=False)
#     def delete(self, request):
#         pk = request.data.get('id')
#         try:
#             order = Order.objects.get(pk=pk)
#         except Objects.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         if request.method == 'DELETE':
#             order.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)

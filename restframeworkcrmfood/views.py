from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import *
from .serializers import *


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class RoleView(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer




class StatusView(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer



class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemView(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class TableView(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer



class MealView(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer



class MealCategoryView(viewsets.ModelViewSet):
    queryset = MealCategory.objects.all()
    serializer_class = MealCategorySerializer



class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class CheckModelView(viewsets.ModelViewSet):
    queryset = CheckModel.objects.all()
    serializer_class = CheckModelSerializer


class ServicePercentageView(viewsets.ModelViewSet):
    queryset = ServicePercentage.objects.all()
    serializer_class = ServicePercentageSerializer


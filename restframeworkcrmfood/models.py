import datetime
from django.db import models
# from django.db.models import Sum, Min, Max, Avg
# from django.contrib.contenttypes.fields import GenericRelation


class Role(models.Model):
    name = models.CharField(max_length=80, default='')
    
    def __str__(self):
        return self.name



class User(models.Model):
    name = models.CharField(max_length=80, default='')
    surname = models.CharField(max_length=80, default='')
    login = models.CharField(max_length=80, default='')
    password = models.CharField(max_length=80, default='')
    email = models.EmailField()
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, related_name='role', default='')
    date_of_add = models.DateField()
    phone = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.name
    
    

class Status(models.Model):
    name = models.CharField(max_length=80, default='')

    def __str__(self):
        return self.name


class Table(models.Model):
    name = models.CharField(max_length=80, default='')

    def __str__(self):
        return self.name



class Order(models.Model):
    orderNumber = models.CharField(max_length=80, default='Order #')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default='')
    # waiter = models.CharField(max_length=80, default='')
    waiter = models.ForeignKey(
        User, on_delete=models.CASCADE, default='', limit_choices_to={'role': 1})
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default='')
    is_it_open = models.BooleanField(default=True)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.orderNumber


class Department(models.Model):
    name = models.CharField(max_length=80, default='')

    def __str__(self):
        return self.name


class MealCategory(models.Model):
    name = models.CharField(max_length=80, default='')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default='')
        
    def __str__(self):
        return self.name



class Meal(models.Model):
    name = models.CharField(max_length=80, default='')
    price = models.CharField(max_length=80, default='')
    description = models.CharField(max_length=80, default='')
    category = models.ForeignKey(
        MealCategory, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.name



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default='')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, default='')
    mealCount = models.IntegerField(default='1')

    def __str__(self):
        name = str(self.order) + ', ' + str(self.meal)
        return name

            

class ServicePercentage(models.Model):
    percentage = models.CharField(max_length=80, default='')

    def __str__(self):
        return self.percentage



class CheckModel(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default='')
    service_fee = models.CharField(max_length=80, default='5')
    orderedMeals = models.ManyToManyField(
        OrderItem)
    service_percentage = models.ForeignKey(ServicePercentage, on_delete=models.CASCADE, default='')
    date = models.DateField()
    total_sum = models.CharField(max_length=80, default='')

    def __str__(self):
        name = 'Check for ' + str(self.order)
        return name







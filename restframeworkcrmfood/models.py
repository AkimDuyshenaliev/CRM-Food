# from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token


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
    
    




# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# class UserToken(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(User=instance)


class Status(models.Model):
    name = models.CharField(max_length=80, default='')

    def __str__(self):
        return self.name


class Table(models.Model):
    name = models.CharField(max_length=80, default='')

    def __str__(self):
        return self.name



class Order(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default='')
    waiter = models.CharField(max_length=80, default='')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default='')
    is_it_open = models.BooleanField(default=True)
    order_date = models.DateField()

    def __str__(self):
        return 'Order'


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
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, default='')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default='')



class ServicePercentage(models.Model):
    percentage = models.CharField(max_length=80, default='')

    def __str__(self):
        return 'Percentage'



class CheckModel(models.Model):
    # check_id = models.AutoField()
    # order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_id', default='')
    date = models.DateField()

    service_fee = models.CharField(max_length=80, default='')
    total_sum = models.CharField(max_length=80, default='')
    meals = models.ManyToManyField(Meal)
    service_percentage = models.ForeignKey(ServicePercentage, on_delete=models.CASCADE, default='')

    def __str__(self):
        return 'Check model'








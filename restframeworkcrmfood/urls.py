from django.urls import path, include
from django.views.generic import TemplateView

from django.urls import path

from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', UserView)
router.register('role', RoleView)
router.register('status', StatusView)
router.register('order', OrderView)
router.register('orderItem', OrderItemView)
router.register('table', TableView)
router.register('meal', MealView)
router.register('meal_category', MealCategoryView)
router.register('department', DepartmentView)
router.register('check', CheckModelView)
router.register('service_percentage', ServicePercentageView)

urlpatterns = [
    path('', include(router.urls)),
]

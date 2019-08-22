from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', views.UserView)
router.register('role', views.RoleView)
# router.register('user_token', views.UserTokenView)
router.register('status', views.StatusView)
router.register('order', views.OrderView)
router.register('table', views.TableView)
router.register('meal', views.MealView)
router.register('meal_category', views.MealCategoryView)
router.register('department', views.DepartmentView)
router.register('check', views.CheckModelView)
router.register('service_percentage', views.ServicePercentageView)

urlpatterns = [
    path('', include(router.urls))
]

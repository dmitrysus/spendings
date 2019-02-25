from django.urls import path
from rest_framework import routers

from .views import ExpenseCategoryViewSet, ExpenseViewSet

router = routers.DefaultRouter()
router.register(r'category', ExpenseCategoryViewSet)
router.register(r'expense', ExpenseViewSet)


urlpatterns = [

]

urlpatterns += router.urls
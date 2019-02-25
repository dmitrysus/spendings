from django.db import models
from django.db.models import Sum

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    @property
    def all_expenses(self):
        return self.expenses.all().aggregate(Sum('value'))


class Expense(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    value = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='expenses', on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.value)

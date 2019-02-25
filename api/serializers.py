from rest_framework import serializers
from core.models import Category, Expense


class CategorySerializer(serializers.ModelSerializer):
    expenses = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('title', 'pk', 'expenses')

    def get_expenses(self, obj):
        expenses = obj.all_expenses.get('value__sum')
        return expenses if expenses else 0


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('value', 'category')
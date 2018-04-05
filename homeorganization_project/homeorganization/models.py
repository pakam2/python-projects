from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Expenses(models.Model):
    amount_of_money = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    type_of_expense = models.CharField(max_length=64, null=False)
    month_of_expense = models.IntegerField(null=False)
    year_of_expense = models.IntegerField(null=False)

class RepeatableExpenses(models.Model):
    amount_of_money = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    type_of_expense = models.CharField(max_length=64, null=False)
    month_of_expense = models.IntegerField(null=False)
    year_of_expense = models.IntegerField(null=False)

class Income(models.Model):
    amount_of_money = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    type_of_income = models.CharField(max_length=64, null=False)
    month_of_income = models.IntegerField(null=False)
    year_of_income = models.IntegerField(null=False)


class ToDoModel(models.Model):
    task_text = models.TextField(null=False)
    whos_task = models.CharField(max_length=64, null=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    def get_absolute_url(self):
        return reverse('todo-delete-view', kwargs={'pk': self.pk})

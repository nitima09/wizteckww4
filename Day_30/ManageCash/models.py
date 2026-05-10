from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInfoModel(AbstractUser):
    def __str__(self):
        return f'{self.username}'


class AddCashModel(models.Model):
    user= models.ForeignKey(
       UserInfoModel,
        on_delete=models.CASCADE,
        related_name='cash_info',
        null= True
    )
    source = models.CharField(max_length=200,null=True)
    datetime = models.DateTimeField(null=True)
    amount = models.FloatField(max_length=100,null=True)
    description = models.TextField(null=True)
    def __str__(self):
        return f'{self.user}'


class ExpenseModel(models.Model):
    user = models.ForeignKey(
        UserInfoModel,
        on_delete=models.CASCADE,
        related_name='expense_info',
        null = True
    )
    description = models.TextField(null=True)
    amount = models.FloatField(max_length=100,null=True)
    datetime = models.DateTimeField(null=True)
    
    def __str__(self):
        return f'{self.user}'
    
    
from django.db import models

class Expense(models.Model):
     amount = models.FloatField(default=0.00)
     category = models.CharField(max_length=100)
     description = models.CharField(max_length=200)
     date = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.category

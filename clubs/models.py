from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=200)
    money = models.IntegerField()

    def __str__(self):
        return f"{self.name}-{self.money}"
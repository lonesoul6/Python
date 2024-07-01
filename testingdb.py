from django.db import models

class YourModelName(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    field3 = models.DateField()

    def __str__(self):
        return self.field1

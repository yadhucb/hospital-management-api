from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=55)
    brand = models.CharField(max_length=55)
    qty = models.PositiveIntegerField()

    def __str__(self):
        return self.name

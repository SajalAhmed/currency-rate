from statistics import mode
from django.db import models

class Convert(models.Model):
    base_currency = models.CharField(max_length=199)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-id', )
    def __str__(self):
        return self.date

class Currency(models.Model):
    name = models.CharField(max_length=199)
    rate = models.CharField(max_length=199)
    convert = models.ForeignKey(Convert, on_delete=models.CASCADE, related_name='currency')

    class Meta:
        ordering = ('-id', )
    def __str__(self):
        return self.name

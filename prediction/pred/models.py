from django.db import models

# Create your models here.
class Clasification(models.Model):
    glass = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

class InputData(models.Model):
    ri = models.FloatField()
    na = models.FloatField()
    mg = models.FloatField()
    al = models.FloatField()
    si = models.FloatField()
    k = models.FloatField()
    ca = models.FloatField()
    ba = models.FloatField()
    fe = models.FloatField()
    prediction = models.ForeignKey(Clasification, on_delete='cascade')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')





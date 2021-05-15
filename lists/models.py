from django.db import models


# Create your models here.
class Item(models.Model):
    text = models.TextField(default='')


class ListPriority(models.Model):
    ds_item = models.CharField(max_length=200)
    id_prioridade = models.IntegerField()
    ds_prioridade = models.CharField(max_length=200)

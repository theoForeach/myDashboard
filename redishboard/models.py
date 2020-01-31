from django.db import models


class Filter(models.Model):
    name = models.CharField(max_length=100)

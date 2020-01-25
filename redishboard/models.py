from django.db import models


class Connection(models.Model):
    host = models.CharField(max_length=100, default='localhost')
    port = models.IntegerField(default=6379)
    db_id = models.IntegerField(default=0)

    def __str__(self):
        return self.host


class Filter(models.Model):
    name = models.CharField(max_length=100)

from django.db import models
from django.contrib.postgres.fields import JSONField


class Cif(models.Model):

    number = models.CharField(max_length=200)
    created = models.DateTimeField('date created')
    modified = models.DateTimeField('date modified')
    data = JSONField()

    def __str__(self):
        return self.number

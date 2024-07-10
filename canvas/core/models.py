from django.db import models

# Create your models here.
class Stand(models.Model):
    title = models.TextField(default=None,unique=True)
    height = models.IntegerField(default=None)
    width = models.IntegerField(default=None)

    def __str__(self):
        return self.title
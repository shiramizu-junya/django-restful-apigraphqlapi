from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField()
    count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

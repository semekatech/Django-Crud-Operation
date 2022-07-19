from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=60)
    picture=models.ImageField()
    author=models.CharField(max_length=60)
    email=models.EmailField(blank=True)
    describe=models.TextField(default='Book')
    def __str__(self):
        return self.name
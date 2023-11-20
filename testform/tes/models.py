from django.db import models

# Create your models here.
class smartForm(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    body = models.TextField()

    def __str__(self):
        return self.title
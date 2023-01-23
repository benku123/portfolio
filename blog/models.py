from django.db import models

# Create your models here
class Portfolio(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    img = models.ImageField()
    url = models.URLField(max_length=250, null=True)

    def __str__(self):
        return self.title
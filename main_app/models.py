from django.db import models

# Create your models here.
class Links(models.Model):
    full_link = models.CharField(max_length=500)
    short_link = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.full_link}: {self.short_link}'

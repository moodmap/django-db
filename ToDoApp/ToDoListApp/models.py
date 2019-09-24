from django.db import models

class People(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    single = models.BooleanField(default=True)

    def __str__(self):
        return (self.first_name, self.last_name)

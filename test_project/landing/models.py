from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):  # название в админке
        # return self.id
        return self.email
    class Meta: # название класса в единственном и множественном числе
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"
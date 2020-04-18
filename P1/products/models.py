from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    title  = models.CharField(max_length = 12)
    description  = models.TextField(max_length = 50, blank= True)
    price  = models.IntegerField()
    discount = models.FloatField(default=2.66)
    mail_id = models.EmailField()



    def get_abs_path(self):
        return reverse('lookup', kwargs={'my_id': self.id})
        # f'/LookUp/{self.id}/'



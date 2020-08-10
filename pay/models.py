from django.db import models
from datetime import date ,datetime
from django.utils import timezone

# Create your models here.
class Cards(models.Model):
    id = models.AutoField
    number= models.IntegerField(blank=False, null= False, unique=True)
    expirationMonth= models.IntegerField(blank=False, null= False)
    expirationYear = models.IntegerField(blank=False, null= False)
    cvv = models.IntegerField(blank=False, null= False)

    def __str__(self):
        return str(self.number)

class Transaction(models.Model):
    id = models.AutoField
    amount = models.IntegerField(blank=False, null= False)
    currency = models.CharField(blank=False, null= False, max_length=4)
    paytype = models.CharField(blank=False, null= False, max_length=10)
    number= models.ForeignKey(to = Cards,blank=False, null= False, on_delete=models.CASCADE)
    status = models.CharField(blank=False, null= False, max_length=10)
    create_datetime = models.DateTimeField(default = timezone.now())
    authorization_code = models.CharField(blank=False, null= False, max_length=20, default="1234567812345678")

    def __str__(self):
        return str(self.id)



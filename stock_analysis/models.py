from django.db import models
import os
import django.db.models
# from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Stock(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.code
    
class Transaction(models.Model):
    stock = models.ForeignKey('Stock', on_delete=django.db.models.DO_NOTHING)
    amount = models.IntegerField()
    price = models.FloatField()
    timestamp = models.DateTimeField()
    
    def __unicode__(self):
        if self.amount>0:
            sell_or_buy = 'bought'
        else:
            sell_or_buy = 'sold'
            
        return '%s %d %s at $%.2f on %s' %(sell_or_buy, self.amount, self.stock.code, self.price, str(self.timestamp).split()[0])
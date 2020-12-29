from django.db import models


# Create your models here.

class Order(models.Model):
    products = models.ManyToManyField('shop.Product', null=False)
    total_amount = models.DecimalField(default=0.00, decimal_places=2, max_digits=30)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

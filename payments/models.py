from django.db import models

# Create your models here.

PAYMENT_STATUS = (
    ('pending', 'Pending'),
    ('success', 'Success'),
    ('failed', 'Failed'),
    ('refunded', 'Refunded'),
)

PAYMENT_METHOD = (
    ('sslcommerz', 'SSL Commerz'),
    ('bkash', 'BKash'),
    ('nagad', 'Nagad'),
    ('rocket', 'Rocket'),
)


class Payments(models.Model):
    order = models.OneToOneField('orders.Order', null=False, on_delete=models.CASCADE)
    status = models.CharField(choices=PAYMENT_STATUS, default='pending', max_length=20)
    method = models.CharField(choices=PAYMENT_METHOD, default=None, max_length=20)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

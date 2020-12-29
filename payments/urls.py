
from django.urls import path
from .views import *

app_name = 'payments'
urlpatterns = [
    path('initiate/', payment_sslcommerz, name='initiate_payment'),
]

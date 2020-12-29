
from django.urls import path
from .views import *
urlpatterns = [
    path('initiate/', payment_sslcommerz),
]

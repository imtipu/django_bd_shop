from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class PaymentsConfig(AppConfig):
    name = 'payments'


# class SSLCommerzPaymentsConfig(AdminConfig):
#     # name = 'ssl_commerz'
#     verbose_name = 'ssl_commerz'
#     default_site = 'payments.admin.PaymentAdminSite'


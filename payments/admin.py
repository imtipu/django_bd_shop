from django.contrib import admin
from django.urls import path

from .admin_views import *
from .models import *


def get_admin_urls(urls):
    def get_urls():
        my_urls = [
            path('payments/transactions/', SSLCommerzTransactionList.as_view(), name='transaction_list')
        ]
        return my_urls + urls

    return get_urls


# @admin.register(Payments, )
# class PaymentsAdmin(admin.ModelAdmin):


# admin_site = PaymentAdminSite()


@admin.register(Payments)
class PaymentModels(admin.ModelAdmin):
    list_display = ['order', 'status', 'method', 'created']


admin.autodiscover()
admin_urls = get_admin_urls(admin.site.get_urls())
admin.site.get_urls = admin_urls

from django.views.generic.base import View, TemplateView


# from django.views import View


class SSLCommerzTransactionList(TemplateView):
    template_name = 'payments/admin/transaction_list.html'

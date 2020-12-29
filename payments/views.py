from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from sslcommerz_lib import SSLCOMMERZ
from django.conf import settings

# Create your views here.
from orders.models import Order
from shop.models import Product


def payment_sslcommerz(request):
    product = Product.objects.get(id=request.GET.get('product'))
    # order = Order.objects.create(
    #     total_amount=product.price
    # )
    # order.products.add(product)
    # order.save()
    success_url = request.build_absolute_uri(reverse('home:shop_home'))
    if product:
        ssl_settings = {
            'store_id': settings.SSL_STORE_ID,
            'store_pass': settings.SSL_STORE_PASSWORD,
            'issandbox': True
        }
        sslcommez = SSLCOMMERZ(ssl_settings)

        post_body = {
            'total_amount': product.price,
            'currency': 'BDT',
            'tran_id': 1,
            'success_url': success_url,
            'fail_url': success_url,
            'cancel_url': success_url,
            'emi_option': 0,
            'cus_name': 'Test',
            'cus_email': 'test@test.com',
            'cus_phone': '01700000000',
            'cus_add1': 'customer address',
            'cus_city': 'Dhaka',
            'cus_country': 'BD',
            'shipping_method': 'NO',
            'multi_card_name': '',
            'num_of_item': 1,
            'product_name': product.title,
            'product_category': 'product_category',
            'product_profile': 'general',
        }
        # post_body['total_amount'] = 100.26
        # post_body['currency'] = "BDT"
        # post_body['tran_id'] = "12345"
        # post_body['success_url'] = "your success url"
        # post_body['fail_url'] = "your fail url"
        # post_body['cancel_url'] = "your cancel url"
        # post_body['emi_option'] = 0
        # post_body['cus_name'] = "test"
        # post_body['cus_email'] = "test@test.com"
        # post_body['cus_phone'] = "01700000000"
        # post_body['cus_add1'] = "customer address"
        # post_body['cus_city'] = "Dhaka"
        # post_body['cus_country'] = "Bangladesh"
        # post_body['shipping_method'] = "NO"
        # post_body['multi_card_name'] = ""
        # post_body['num_of_item'] = 1
        # post_body['product_name'] = "Test"
        # post_body['product_category'] = "Test Category"
        # post_body['product_profile'] = "general"
        response = sslcommez.createSession(post_body)
        print(response)
        # return JsonResponse(response, safe=False)
        return render(request, 'payments/initiate.html', {'response': response})

    return JsonResponse(status=400, safe=True)

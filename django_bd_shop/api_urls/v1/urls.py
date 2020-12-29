from django.urls import path, include

urlpatterns = [
    path('payments/', include('payments.api.v1.urls'))
]

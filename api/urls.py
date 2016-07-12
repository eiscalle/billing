from django.conf.urls import url, include
from django.contrib import admin

from api.views import BillingUserView, OrderListView

urlpatterns = [
    url(r'^user/(?P<user_id>[a-zA-Z0-9]+)/', BillingUserView.as_view(), name='user_detail'),
    url(r'^orders/(?P<user_id>[a-zA-Z0-9]+)/', OrderListView.as_view(), name='order_list'),
]
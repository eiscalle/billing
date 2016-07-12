from django.shortcuts import render
from rest_framework import serializers

from api.models import BillingUser, Order


class BillingUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingUser
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
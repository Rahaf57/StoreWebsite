from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Customer(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

    def validate(self, attrs):
        unknown = set(self.initial_data) - set(self.fields)
        if unknown:
            raise ValidationError("Unknown field(s): {}".format(", ".join(unknown)))
        return attrs


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customerID', 'productID', 'quantity', 'created_at']

    def validate(self, attrs):
        unknown = set(self.initial_data) - set(self.fields)
        if unknown:
            raise ValidationError("Unknown field(s): {}".format(", ".join(unknown)))
        return attrs


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'customerID', 'productID', 'rating', 'review']

    def validate(self, attrs):
        unknown = set(self.initial_data) - set(self.fields)
        if unknown:
            raise ValidationError("Unknown field(s): {}".format(", ".join(unknown)))
        return attrs

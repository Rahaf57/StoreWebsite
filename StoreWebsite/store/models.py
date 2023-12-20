from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):

    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.customerID} - {self.productID} - {self.quantity} units"


class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    review = models.TextField()

    def __str__(self):
        return f"Review {self.id} - {self.customerID} - {self.productID} - {self.rating} Stars"

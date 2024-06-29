from django.db import models


class User(models.Model):
   
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
   
    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    image_file = models.FileField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Cart for {self.user.username}"

    def total_price(self):
        return self.quantity * self.product.price
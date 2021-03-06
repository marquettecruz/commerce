from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model


class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.category}"

class Image(models.Model):
    name = models.CharField(max_length=500)
    imageFile = models.FileField(upload_to='images/', null=True, verbose_name="")

    def __str__(self) -> str:
        return self.name + ":" + str(self.imageFile)

class User(AbstractUser):
    pass

  
class Product(models.Model):
    product_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="product_owner")
    product_name = models.CharField(max_length=64)
    product_description = models.CharField(max_length=254)
    product_price = models.DecimalField(decimal_places=2, max_digits=10)
    product_picture = models.ForeignKey(Image, on_delete=models.CASCADE,  related_name="product_images")
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product_category")
    product_date = models.DateTimeField(auto_now_add=True, blank=True)
    product_active = models.BooleanField(default=True)
    product_winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="product_winner", null=True, blank=True)


    def __str__(self) -> str:
        return f"{self.product_name} {self.product_price}$ {self.product_owner}"

class Comment(models.Model):
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user", null=True, blank=True)
    comment_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="coment_product", null=True, blank=True)
    comment_text = models.CharField(max_length=500)
    comment_date = models.DateTimeField(auto_now_add=True, blank=True) 

    
    def __str__(self) -> str:
       return f"{self.comment_user} {self.comment_product.name} {self.comment_text}"

class Bid(models.Model):
    bid_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="bid_product")
    bid_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid_user")
    bid_price = models.DecimalField(decimal_places=2, max_digits=10)
    bid_date = models.DateTimeField(auto_now_add=True)
    bid_comments = models.ManyToManyField(Comment, blank=True, related_name="bid_comments")


    def __str__(self) -> str:
        return f"{self.bid_user} {self.bid_product.name} {self.bid_price}"  
    




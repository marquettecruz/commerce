from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model


class Category(models.Model):
    category = models.CharField(max_length=64)

class User(AbstractUser):
    watchingProduct = models.ManyToOneRel(Product, on_delete=models.CASCADE, blank=True, related_name="productWatchList")

    def __str__(self) -> str:
        return super().__str__()

class Product(models.Model):
    owner = models.ForeignKey(User, related_name="owner")
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=254)
    price = models.DecimalField(decimal_places=2)
    picture = models.ForeignKey(Images, on_delete=models.CASCADE,  related_name="images")
    category = models.ForeignKey(Category, related_name="category")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    active = models.BooleanField(default=True)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='winner', null=True, blank=True)


    def __str__(self) -> str:
        return f"{self.name} {self.starting_bid}$ {self.owner}"

class Bid(models.Model):
    product_bid = models.ForeignKey(Product, related_name="product")
    user_bid = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bid")
    price_bid = models.DecimalField(decimal_places=2)
    date_bid = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToOneRel(Comment, on_delete=models.CASCADE, blank = True, related_name="comments")


    def __str__(self) -> str:
        return f"{self.user_bid} {self.product_bid.name} {self.price_bid}"  
    
class Comment(models.Model):
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment', null=True, blank=True)
    product_comment = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_comment', null=True, blank=True)
    text_comment = models.CharField(max_length=500)
    date_comment = models.DateTimeField(auto_now_add=True, blank=True) 

    def __str__(self) -> str:
       return f"{self.user_comment} {self.product_comment.name} {self.text_comment}"

class Images(models.Model):
    name = models.CharField(max_length=500)
    imageFile = models.FileField(upload_to='images/', null=True, verbose_name="")

    def __str__(self) -> str:
        return self.name + ":" + str(self.imageFile)
from typing import Iterable, Optional
from django.db import models
from django.utils.text import slugify
from authentication.models import CustomUser

class BaseModel(models.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Catigory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True)
 
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        super(Catigory, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title 

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    description = models.TextField(null=True)
    quantity = models.PositiveBigIntegerField(default=0)
    category = models.ForeignKey(to=Catigory, on_delete=models.CASCADE, related_name="products")
    image = models.ImageField(upload_to="products/%Y/%m/%d/", null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title + " Catigory_id - " + str(self.category)
    

class Order(BaseModel):
    NEW = 'new'
    CONFIRMED = 'confirmed'
    CANCELED = 'canceled'

    ORDER_STATUS = (
        (NEW, 'New'),
        (CONFIRMED, 'Confirmed'),
        (CANCELED, 'Canceled')
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    total_price = models.DecimalField(decimal_places=2, max_digits=12)
    status = models.CharField(choices=ORDER_STATUS, default=NEW, max_length=50)
    paid = models.BooleanField(default=False)

class OrderProduct(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="products")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_products")
    quantity = models.PositiveBigIntegerField()

    def update_quantity(self):
        self.product.quantity -= self.quantity
        self.product.save()

    def save(self, *args, **kwargs) -> None:
        if not self.pk:
            self.update_quantity() 
        super(OrderProduct, self).save( *args, **kwargs)
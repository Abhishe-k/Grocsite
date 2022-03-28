from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone


class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    type = models.ForeignKey(Type, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)
    desc = models.TextField(blank=True, null=True)
    interested = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "name: {0}, type: {1}, price: {2}, stock: {3}".format(self.name, self.type, self.price, self.stock)

    def topup(self):
        self.stock += 200

class Client(User):
    CITY_CHOICES = [('WD', 'Windsor'), ('TO', 'Toronto'), ('CH', 'Chatham'), ('WL', 'WATERLOO')]
    # fullname = models.CharField(max_length=50)
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='CH')
    interested_in = models.ManyToManyField(Type)
    phone = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return "username: {0}, Address: {1}, City: {2}, Interests: {3}".format(self.username, self.shipping_address,
                                                                               self.city, self.interested_in)


class OrderItem(models.Model):
    item = models.ForeignKey(Item, related_name='OrderItems', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    qty_ordered = models.IntegerField()
    STATUS_CHOICES = [(0, 'Cancelled'), (1, 'Placed'), (2, 'Shipped'), (3, 'Delivered')]
    status = models.IntegerField(choices=STATUS_CHOICES)
    date = models.DateField(null=True, blank=True)

    def total_price(self):
        return self.qty_ordered * Item.objects.get(self.item).price

    def __str__(self):
        return "username: {0}, Item: {1}, Qty: {2}".format(self.client.username, self.item, self.qty_ordered)

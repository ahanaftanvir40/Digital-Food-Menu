from django.db import models


# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length = 200)
    item_desc = models.CharField(max_length = 1000)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length = 1000, default= 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtZekdRzYGc99Ck2T6eX5xhHbWRT4IEzNfAHzaQq9ms5dqvczFUIZJJ5gqjx8joBRFK_8&usqp=CAU')

# Generated by Django 5.0 on 2023-12-24 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtZekdRzYGc99Ck2T6eX5xhHbWRT4IEzNfAHzaQq9ms5dqvczFUIZJJ5gqjx8joBRFK_8&usqp=CAU', max_length=1000),
        ),
    ]

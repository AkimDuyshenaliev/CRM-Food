# Generated by Django 2.2.2 on 2019-09-04 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restframeworkcrmfood', '0013_auto_20190905_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkmodel',
            name='orderedMeals',
        ),
        migrations.AddField(
            model_name='checkmodel',
            name='orderedMeals',
            field=models.ManyToManyField(to='restframeworkcrmfood.OrderItem'),
        ),
    ]

# Generated by Django 2.2.2 on 2019-09-04 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restframeworkcrmfood', '0007_auto_20190904_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='mealCount',
            field=models.IntegerField(default='1'),
        ),
    ]

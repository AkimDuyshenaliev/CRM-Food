# Generated by Django 2.2.2 on 2019-09-04 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restframeworkcrmfood', '0003_auto_20190904_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='waiter',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='restframeworkcrmfood.User'),
        ),
    ]

# Generated by Django 2.2.2 on 2019-08-12 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restframeworkcrmfood', '0005_auto_20190812_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkmodel',
            name='order_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='order_id', to='restframeworkcrmfood.Order'),
        ),
    ]
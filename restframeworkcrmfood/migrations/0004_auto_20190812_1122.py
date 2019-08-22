# Generated by Django 2.2.2 on 2019-08-12 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restframeworkcrmfood', '0003_auto_20190812_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_id',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='restframeworkcrmfood.Status'),
        ),
    ]

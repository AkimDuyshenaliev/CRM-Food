# Generated by Django 2.2.2 on 2019-09-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restframeworkcrmfood', '0010_checkmodel_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkmodel',
            name='service_fee',
            field=models.CharField(default='5%', max_length=80),
        ),
    ]

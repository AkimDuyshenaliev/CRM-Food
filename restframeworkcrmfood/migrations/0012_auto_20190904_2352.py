# Generated by Django 2.2.2 on 2019-09-04 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restframeworkcrmfood', '0011_auto_20190904_2349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkmodel',
            name='meals',
        ),
        migrations.AddField(
            model_name='checkmodel',
            name='orderedMeals',
            field=models.ForeignKey(default='', limit_choices_to={'order': models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='restframeworkcrmfood.Order')}, on_delete=django.db.models.deletion.CASCADE, to='restframeworkcrmfood.OrderItem'),
        ),
    ]

# Generated by Django 4.0.5 on 2022-08-07 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_bookincart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookincart',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Createtime'),
        ),
        migrations.AlterField(
            model_name='bookincart',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Updatetime'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Create time'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Update time'),
        ),
    ]

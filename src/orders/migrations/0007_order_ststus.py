# Generated by Django 4.0.5 on 2022-08-20 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ststus',
            field=models.CharField(choices=[('Y', 'Обработан'), ('N', 'Необработан'), ('D', 'Отправлен')], default='Y', max_length=50, verbose_name='Status'),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.0 on 2024-01-03 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_transaction_is_bancrupt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='is_bancrupt',
        ),
    ]
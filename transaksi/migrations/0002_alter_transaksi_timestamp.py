# Generated by Django 3.2.9 on 2021-12-04 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaksi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaksi',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
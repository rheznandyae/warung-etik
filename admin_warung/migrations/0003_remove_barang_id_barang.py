# Generated by Django 3.2.9 on 2021-12-04 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_warung', '0002_auto_20211204_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barang',
            name='id_barang',
        ),
    ]

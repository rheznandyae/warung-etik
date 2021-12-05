# Generated by Django 3.2.9 on 2021-12-04 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('id_barang', models.IntegerField()),
                ('harga', models.PositiveIntegerField()),
                ('stok', models.PositiveIntegerField()),
                ('terjual', models.PositiveIntegerField()),
                ('deskripsi', models.TextField()),
            ],
        ),
    ]

# Generated by Django 3.0.4 on 2021-05-01 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdHD_A4', models.CharField(max_length=10)),
                ('pdMD_A4', models.CharField(max_length=10)),
                ('pdHD_A3', models.CharField(max_length=10)),
                ('pdMD_A3', models.CharField(max_length=10)),
                ('wcA4', models.CharField(max_length=10)),
                ('wcA3', models.CharField(max_length=10)),
                ('caA4', models.CharField(max_length=10)),
                ('caA3', models.CharField(max_length=10)),
            ],
        ),
    ]
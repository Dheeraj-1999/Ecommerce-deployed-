# Generated by Django 2.0.3 on 2018-07-14 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jumpkart', '0003_product_pid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('des', models.CharField(max_length=345)),
                ('rating', models.IntegerField()),
                ('img', models.CharField(max_length=300)),
                ('price', models.CharField(max_length=300)),
                ('category', models.CharField(max_length=300)),
                ('specify', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'CartTable',
            },
        ),
    ]
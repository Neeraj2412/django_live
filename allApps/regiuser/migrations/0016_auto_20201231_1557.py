# Generated by Django 3.1.4 on 2020-12-31 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regiuser', '0015_auto_20201231_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herbproduct',
            name='productImage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

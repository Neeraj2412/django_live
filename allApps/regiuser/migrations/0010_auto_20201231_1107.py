# Generated by Django 3.1.4 on 2020-12-31 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regiuser', '0009_auto_20201231_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herbproduct',
            name='sellername',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='regiuser.sellerprofile'),
        ),
    ]

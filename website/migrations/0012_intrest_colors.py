# Generated by Django 3.1 on 2020-09-07 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20200907_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='intrest',
            name='colors',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
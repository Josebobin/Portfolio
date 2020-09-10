# Generated by Django 3.1 on 2020-09-06 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20200903_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Socialiconlink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb', models.URLField(blank=True, max_length=100, null=True)),
                ('insta', models.URLField(blank=True, max_length=100, null=True)),
                ('link', models.URLField(blank=True, max_length=100, null=True)),
                ('addr', models.CharField(blank=True, max_length=150, null=True)),
                ('mob', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='experience',
            name='tags',
            field=models.ManyToManyField(blank=True, max_length=150, null=True, to='website.Tag'),
        ),
    ]
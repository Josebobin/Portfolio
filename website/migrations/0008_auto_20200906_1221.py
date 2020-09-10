# Generated by Django 3.1 on 2020-09-06 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20200906_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='HappyCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clients', models.CharField(blank=True, max_length=100, null=True)),
                ('projects', models.CharField(blank=True, max_length=100, null=True)),
                ('hours', models.CharField(blank=True, max_length=100, null=True)),
                ('workers', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Intrest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(blank=True, max_length=100, null=True)),
                ('intrest', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='socialiconlink',
            options={'verbose_name': 'contactus', 'verbose_name_plural': 'contact_website'},
        ),
    ]
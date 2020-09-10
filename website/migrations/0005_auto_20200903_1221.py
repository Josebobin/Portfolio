# Generated by Django 3.1 on 2020-09-03 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20200903_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='education_title',
            field=models.CharField(blank=True, choices=[('B.Sc. Computer Science', 'B.Sc. Computer Science'), ('Diploma in Web Designing', 'Diploma in Web Designing')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='education_university',
            field=models.CharField(blank=True, choices=[('University of Kerala', 'University of Kerala'), ('Arena Multimedia Kochi', 'Arena Multimedia Kochi')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='eexperiencemore',
            name='more_details1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='experience_company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

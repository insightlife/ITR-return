# Generated by Django 4.0.2 on 2022-03-03 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itrrequest',
            name='form16',
            field=models.FileField(blank=True, default='Upload form 16 here', upload_to=''),
        ),
    ]
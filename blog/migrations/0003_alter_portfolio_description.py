# Generated by Django 4.1.5 on 2023-01-21 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_portfolio_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]

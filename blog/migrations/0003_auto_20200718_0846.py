# Generated by Django 3.0.8 on 2020-07-18 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200718_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogtable',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

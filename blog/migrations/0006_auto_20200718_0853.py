# Generated by Django 3.0.8 on 2020-07-18 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200718_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogtable',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Author'),
        ),
    ]
# Generated by Django 2.2 on 2020-09-15 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200915_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredproperty',
            name='link',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='investproperties',
            name='link',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]

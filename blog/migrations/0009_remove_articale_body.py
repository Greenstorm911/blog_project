# Generated by Django 4.2.7 on 2024-02-12 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_articale_options_articale_genrate_descryption_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articale',
            name='body',
        ),
    ]
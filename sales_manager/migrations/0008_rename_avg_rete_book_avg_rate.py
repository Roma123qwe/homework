# Generated by Django 3.2.3 on 2021-05-29 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales_manager', '0007_auto_20210529_1301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='avg_rete',
            new_name='avg_rate',
        ),
    ]

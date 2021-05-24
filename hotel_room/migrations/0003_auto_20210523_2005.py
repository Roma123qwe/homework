# Generated by Django 3.2.3 on 2021-05-23 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel_room', '0002_auto_20210521_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='title',
            field=models.CharField(default='Room', max_length=100),
        ),
        migrations.CreateModel(
            name='Reserv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_from', models.DateField()),
                ('reservation_to', models.DateField()),
                ('what_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reservs', to='hotel_room.room')),
                ('who_reserv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reservs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
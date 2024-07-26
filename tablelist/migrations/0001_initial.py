# Generated by Django 4.1.5 on 2024-07-21 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TableList',
            fields=[
                ('table_id', models.AutoField(primary_key=True, serialize=False)),
                ('table_name', models.CharField(max_length=255)),
                ('table_max_guests', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 4.2.5 on 2024-04-19 06:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website1', '0026_alter_usermodel_organisation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='user_f',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

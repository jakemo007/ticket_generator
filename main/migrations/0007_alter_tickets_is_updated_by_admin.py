# Generated by Django 4.1.4 on 2022-12-15 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_tickets_is_deleted_tickets_is_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='is_updated_by_admin',
            field=models.BooleanField(default=False),
        ),
    ]
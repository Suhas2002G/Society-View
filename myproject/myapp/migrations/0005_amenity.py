# Generated by Django 5.0.6 on 2025-01-11 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_mobile_number_flat_mobile_remove_flat_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.CharField(max_length=100)),
                ('des', models.TextField(db_column='description')),
                ('rent', models.IntegerField()),
            ],
        ),
    ]

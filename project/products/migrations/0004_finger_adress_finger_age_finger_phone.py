# Generated by Django 4.1.7 on 2023-05-02 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_finger_datetime_alter_finger_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='finger',
            name='adress',
            field=models.CharField(default='adress', max_length=100),
        ),
        migrations.AddField(
            model_name='finger',
            name='age',
            field=models.CharField(default='age', max_length=100),
        ),
        migrations.AddField(
            model_name='finger',
            name='phone',
            field=models.CharField(default='phone', max_length=100),
        ),
    ]
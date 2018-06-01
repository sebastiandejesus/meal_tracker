# Generated by Django 2.0.4 on 2018-05-06 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meallogger', '0002_auto_20180506_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='items',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='mealtime',
            field=models.CharField(choices=[('breakfast', 'Breakfast'), ('brunch', 'Brunch'), ('lunch', 'Lunch'), ('snack', 'Snack'), ('dinner', 'Dinner'), ('late snack', 'Late Snack')], default='Breakfast', max_length=20),
        ),
    ]
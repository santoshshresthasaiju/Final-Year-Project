# Generated by Django 4.2.7 on 2023-11-23 07:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Prediction", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="predict",
            name="age",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="predict",
            name="bmi",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="predict",
            name="diabetesPedigree",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="predict",
            name="glucose",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="predict",
            name="insulin",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="predict",
            name="proabability",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="predict",
            name="result",
            field=models.CharField(default="default_value", max_length=15),
        ),
        migrations.AddField(
            model_name="predict",
            name="skinThickness",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="predict",
            name="pregnancy",
            field=models.IntegerField(default=0),
        ),
    ]

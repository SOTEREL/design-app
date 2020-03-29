# Generated by Django 3.0.3 on 2020-03-29 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0005_auto_20200329_1651")]

    operations = [
        migrations.AddField(
            model_name="shape",
            name="zoom",
            field=models.PositiveSmallIntegerField(default=19),
        ),
        migrations.AlterField(
            model_name="featurestyle",
            name="name",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-08 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0010_feature_is_observation")]

    operations = [
        migrations.AddField(
            model_name="feature",
            name="is_important",
            field=models.BooleanField(default=False),
        )
    ]

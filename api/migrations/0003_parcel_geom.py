# Generated by Django 3.0.3 on 2020-02-27 17:13

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_parcel"),
    ]

    operations = [
        migrations.AddField(
            model_name="parcel",
            name="geom",
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
    ]

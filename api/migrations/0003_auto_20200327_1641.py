# Generated by Django 3.0.3 on 2020-03-27 15:41

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [("api", "0002_auto_20200327_1624")]

    operations = [
        migrations.AlterField(
            model_name="circle",
            name="coordinates",
            field=jsonfield.fields.JSONField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="line",
            name="coordinates",
            field=jsonfield.fields.JSONField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="multipolygon",
            name="coordinates",
            field=jsonfield.fields.JSONField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="point",
            name="coordinates",
            field=jsonfield.fields.JSONField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="polygon",
            name="coordinates",
            field=jsonfield.fields.JSONField(blank=True, default=None, null=True),
        ),
    ]
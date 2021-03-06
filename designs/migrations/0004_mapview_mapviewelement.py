# Generated by Django 3.1.3 on 2021-01-12 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("designs", "0003_auto_20210112_1726"),
    ]

    operations = [
        migrations.CreateModel(
            name="MapView",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField(blank=True, default="")),
                (
                    "design",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="designs.design"
                    ),
                ),
            ],
            options={"unique_together": {("design", "name")},},
        ),
        migrations.CreateModel(
            name="MapViewElement",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("z_index", models.PositiveSmallIntegerField(default=0)),
                ("min_zoom", models.PositiveSmallIntegerField(default=0)),
                ("max_zoom", models.PositiveSmallIntegerField(blank=True, null=True)),
                (
                    "map_element",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="designs.mapelement",
                    ),
                ),
                (
                    "view",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="elements",
                        to="designs.mapview",
                    ),
                ),
            ],
        ),
    ]

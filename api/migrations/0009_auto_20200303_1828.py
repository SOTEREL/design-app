# Generated by Django 3.0.3 on 2020-03-03 18:28

import api.models.fields
import api.models.map.line
import api.models.map.polygon
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [("api", "0008_auto_20200303_1804")]

    operations = [
        migrations.CreateModel(
            name="Line",
            fields=[
                (
                    "feature_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="api.Feature",
                    ),
                ),
                (
                    "coordinates",
                    jsonfield.fields.JSONField(
                        validators=[api.models.map.line.validate_coordinates]
                    ),
                ),
            ],
            bases=("api.feature",),
        ),
        migrations.CreateModel(
            name="Point",
            fields=[
                (
                    "feature_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="api.Feature",
                    ),
                ),
                (
                    "lat",
                    api.models.fields.LatField(
                        validators=[
                            django.core.validators.MinValueValidator(80),
                            django.core.validators.MaxValueValidator(90),
                            django.core.validators.MinValueValidator(80),
                            django.core.validators.MaxValueValidator(90),
                        ]
                    ),
                ),
                (
                    "lng",
                    api.models.fields.LngField(
                        validators=[
                            django.core.validators.MinValueValidator(-180),
                            django.core.validators.MaxValueValidator(180),
                            django.core.validators.MinValueValidator(-180),
                            django.core.validators.MaxValueValidator(180),
                        ]
                    ),
                ),
            ],
            bases=("api.feature",),
        ),
        migrations.CreateModel(
            name="Polygon",
            fields=[
                (
                    "feature_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="api.Feature",
                    ),
                ),
                (
                    "coordinates",
                    jsonfield.fields.JSONField(
                        validators=[api.models.map.polygon.validate_coordinates]
                    ),
                ),
            ],
            bases=("api.feature",),
        ),
        migrations.RemoveField(model_name="feature", name="geom"),
        migrations.AlterField(
            model_name="feature",
            name="name",
            field=models.CharField(blank=True, default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="project",
            name="map_lat",
            field=api.models.fields.LatField(
                validators=[
                    django.core.validators.MinValueValidator(80),
                    django.core.validators.MaxValueValidator(90),
                    django.core.validators.MinValueValidator(80),
                    django.core.validators.MaxValueValidator(90),
                    django.core.validators.MinValueValidator(80),
                    django.core.validators.MaxValueValidator(90),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="map_lng",
            field=api.models.fields.LngField(
                validators=[
                    django.core.validators.MinValueValidator(-180),
                    django.core.validators.MaxValueValidator(180),
                    django.core.validators.MinValueValidator(-180),
                    django.core.validators.MaxValueValidator(180),
                    django.core.validators.MinValueValidator(-180),
                    django.core.validators.MaxValueValidator(180),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="map_zoom",
            field=models.PositiveSmallIntegerField(default=19),
        ),
        migrations.CreateModel(
            name="Circle",
            fields=[
                (
                    "point_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="api.Point",
                    ),
                ),
                ("radius", models.PositiveSmallIntegerField()),
            ],
            bases=("api.point",),
        ),
    ]
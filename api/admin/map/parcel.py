from django.contrib import admin

from ..mixins import LinkToProject
from ...forms.map import ParcelForm
from ...models.map import Parcel


@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin, LinkToProject):
    list_display = ("number", "link_to_project", "insee", "section")
    form = ParcelForm

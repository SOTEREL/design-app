from django.contrib import admin

from ...forms.map import FeatureTypeForm
from ...models.map import FeatureType


@admin.register(FeatureType)
class FeatureTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "shape_ctype")
    form = FeatureTypeForm
    prepopulated_fields = {"slug": ("name",)}
    save_on_top = True

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj=obj)
        if obj is not None:
            return (*readonly_fields, "shape_ctype")
        return readonly_fields

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj=obj)
        if obj is None:
            fields.remove("style")
        return fields

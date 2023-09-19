from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from places.models import Place, Image


class PreviewMixin(object):
    def preview(self, image):
        url = image.image.url
        return format_html('<img src="{}" style="max-height: 200px;">', url)


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ['image_preview', ]
    fields = ['image', 'image_preview', 'position']

    def image_preview(self, obj):
        return obj.image_preview


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['title', ]
    inlines = [PlaceImageInline, ]

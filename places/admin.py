from django.contrib import admin
from places.models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin


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


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'image', 'order', 'image_preview')
    raw_id_fields = ('place',)
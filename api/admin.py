from django.contrib import admin
from .models import Dataset, Brand, Link, Source

admin.site.register(Source)
class SourceAdmin(admin.StackedInline):
    model = Source
    extra = 0

    def has_delete_permission(self, request, obj):
        return False

admin.site.register(Link)
class LinkAdmin(admin.StackedInline):
    model = Link
    extra = 0

admin.site.register(Brand)
class BrandAdmin(admin.StackedInline):
    model = Brand
    extra = 0

    def has_delete_permission(self, request, obj):
        return False


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    inlines = [BrandAdmin, LinkAdmin, SourceAdmin]



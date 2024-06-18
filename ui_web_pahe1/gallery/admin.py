from django.contrib import admin

from .models import ProductGallery, HomeGallery


class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = [a.name for a in ProductGallery._meta.fields]
    raw_id_fields = ['product']


class HomeGalleryAdmin(admin.ModelAdmin):
    list_display = [a.name for a in HomeGallery._meta.fields]


admin.site.register(ProductGallery, ProductGalleryAdmin)
admin.site.register(HomeGallery, HomeGalleryAdmin)

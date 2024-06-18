from django.contrib import admin

from .models import (
    ProductItem,
    ProductItemPrice,
    ShoppingCard,
    Coupon,
    ProductCategory
)


class ProductItemAdmin(admin.ModelAdmin):
    list_display = [a.name for a in ProductItem._meta.fields]
    raw_id_fields = ['category']
    list_filter = ['category']


class ProductItemPriceAdmin(admin.ModelAdmin):
    list_display = [a.name for a in ProductItemPrice._meta.fields]
    raw_id_fields = ['product']


class ShoppingCardAdmin(admin.ModelAdmin):
    list_display = [a.name for a in ShoppingCard._meta.fields]
    raw_id_fields = ['user']


class CouponAdmin(admin.ModelAdmin):
    list_display = [a.name for a in Coupon._meta.fields]


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [a.name for a in ProductCategory._meta.fields]
    raw_id_fields = ['parent']


admin.site.register(ProductItem, ProductItemAdmin)
admin.site.register(ProductItemPrice, ProductItemPriceAdmin)
admin.site.register(ShoppingCard, ShoppingCardAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
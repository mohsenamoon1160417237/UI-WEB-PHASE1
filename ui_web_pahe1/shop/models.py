from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

from utils.general_model import GeneralModel


class ProductItem(GeneralModel):
    name = models.CharField(
        max_length=500,
        verbose_name=_("name")
    )
    stock_count = models.PositiveIntegerField(
        default=0,
        verbose_name=_("stock_count")
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_("price")
    )
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        blank=True,
        verbose_name=_("rating")
    )
    reviews_count = models.PositiveIntegerField(
        default=0,
        verbose_name=_("reviews_count")
    )
    colors = models.JSONField(
        verbose_name=_("colors")
    )
    description = models.TextField(
        verbose_name=_("description")
    )
    additional_info = models.JSONField(
        verbose_name=_("additional_info")
    )
    enable_off = models.BooleanField(
        default=False,
        verbose_name=_("enable_off")
    )
    seen_count = models.PositiveIntegerField(
        default=0,
        verbose_name=_("seen_count")
    )


class ProductItemPrice(GeneralModel):
    product = models.ForeignKey(
        to='shop.ProductItem',
        on_delete=models.CASCADE,
        related_name='product',
        verbose_name=_("product")
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_("price")
    )
    is_latest = models.BooleanField(
        default=True,
        verbose_name=_("is_latest")
    )


class ShoppingCard(GeneralModel):
    products_storage = models.JSONField(
        verbose_name=_("products_storage")
    )
    user = models.OneToOneField(
        to='accounts.User',
        on_delete=models.CASCADE,
        related_name='user',
        verbose_name=_("user")
    )


class Coupon(GeneralModel):
    code = models.CharField(
        max_length=500,
        unique=True,
        verbose_name=_("code")
    )
    percentage_amount = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99)],
        null=True,
        blank=True,
        verbose_name=_("percentage_amount"),
    )
    value_amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        blank=True,
        null=True,
        verbose_name=_("value_amount")
    )
    max_percentage = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99)],
        null=True,
        blank=True,
        verbose_name=_("max_percentage"),
    )
    max_value = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        blank=True,
        null=True,
        verbose_name=_("max_value")
    )


class ProductCategory(GeneralModel):
    name = models.CharField(
        unique=True,
        max_length=500,
        verbose_name=_("name")
    )
    parent = models.ForeignKey(
        to='self',
        on_delete=models.SET_NULL,
        related_name='children',
        null=True,
        blank=True,
        verbose_name=_("parent")
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("description")
    )
    enable_off = models.BooleanField(
        default=False,
        verbose_name=_("enable_off")
    )

    def save(self, *args, **kwargs):
        try:
            if self.parent.parent.parent.parent.parent is not None:
                raise ValueError("Reached max depth: 5")
        except Exception:
            super(ProductCategory, self).save(*args, **kwargs)

from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.general_model import GeneralModel


class ProductGallery(GeneralModel):
    product = models.ForeignKey(
        to='shop.ProductItem',
        on_delete=models.CASCADE,
        related_name='product_gallery',
        verbose_name=_("product")
    )
    file = models.FileField(
        verbose_name=_("file"),
        upload_to='images/gallery'
    )


class HomeGallery(GeneralModel):
    file = models.FileField(
        verbose_name=_("file"),
        upload_to='images/gallery'
    )
    index = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("index")
    )

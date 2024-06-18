from django.urls import path

from .views import (
    home,
    product_detail,
    add_to_card,
    delete_from_card
)

urlpatterns = [
    path('', home, name='home'),
    path('<int:pk>/', product_detail, name='product_detail'),
    path('card/', add_to_card, name='card_detail'),
    path('del-card/', delete_from_card, name='del_card')
]

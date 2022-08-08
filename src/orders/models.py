from django.db import models
from django.contrib.auth import get_user_model
from book import models as b_models

User = get_user_model()

class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="carts",
        verbose_name="customer",
        null=True,
        blank=True
    )
    created_date = models.DateTimeField(
        verbose_name="Create time",
        auto_now_add=True,
    )
    update_date = models.DateTimeField(
        verbose_name="Update time",
        auto_now=True
    )

class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.PROTECT,
        related_name="goods",
        verbose_name="Cart",
    )
    book = models.ForeignKey(
        b_models.Book,
        on_delete=models.PROTECT,
        related_name="goods",
        verbose_name="Book",
    )
    quantity = models.SmallIntegerField(
        verbose_name="Quantity",
    )
    price = models.DecimalField(
        verbose_name="Price",
        max_digits=6, 
        decimal_places=2,
        null=True,
        blank=True
    )
    created_date = models.DateTimeField(
        verbose_name="Createtime",
        auto_now_add=True,
    )
    update_date = models.DateTimeField(
        verbose_name="Updatetime",
        auto_now=True
    )



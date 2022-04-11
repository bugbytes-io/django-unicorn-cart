from django.contrib.auth.models import User
from django.db.models import F
from django_unicorn.components import UnicornView, QuerySetType
from core.models import UserItem

class CartView(UnicornView):
    user_products: QuerySetType[UserItem] = None
    user: User
    total: float = 0

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)  # calling super is required
        self.user = kwargs.get("user_pk")
        self.user_products = UserItem.objects.filter(user=self.user)
        self.get_total()

    def add_item(self, product_pk):
        # create useritem
        item, created = UserItem.objects.get_or_create(
            user_id=self.user,
            product_id=product_pk
        )
        if not created:
            item.quantity = F('quantity') + 1
            item.save()
        self.user_products = UserItem.objects.filter(user=self.user)
        self.get_total()

    def get_total(self):
        self.total = sum(product.total_price for product in self.user_products)

    def delete_item(self, product_pk):
        item = UserItem.objects.get(pk=product_pk)
        item.delete()
        self.user_products = self.user_products.exclude(pk=product_pk)
        self.get_total()

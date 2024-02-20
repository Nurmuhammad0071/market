from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product, Price


@receiver(post_save, sender=Product)
def create_price(sender, instance, created, *args, **kwarg):
    if instance.discount_id:
        product_price = Price.objects.all()

        for price in product_price:
            if instance.discount_id.count == 0:
                break
            else:
                price.discount_price = price.price - (price.price * instance.discount_id.discount / 100)
                price.save()

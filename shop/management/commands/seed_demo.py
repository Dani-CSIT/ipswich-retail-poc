# shop/management/commands/seed_demo.py
from django.core.management.base import BaseCommand
from shop.models import Product

class Command(BaseCommand):
    help = "Seed demo products (idempotent)."

    def handle(self, *args, **kwargs):
        items = [
            dict(sku="SKU1", name="Demo Jacket", price=59.99, stock=10),
            dict(sku="SKU2", name="City Backpack", price=39.99, stock=20),
        ]
        for item in items:
            obj, created = Product.objects.get_or_create(sku=item["sku"], defaults=item)
            if not created:
                for k, v in item.items():
                    setattr(obj, k, v)
                obj.save()
        self.stdout.write(self.style.SUCCESS("Demo products ensured."))
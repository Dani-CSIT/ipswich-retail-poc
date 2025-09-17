import pytest

from shop.models import Product


@pytest.mark.django_db
def test_product_str():
    p = Product.objects.create(sku="T1", name="Test", price=1.23, stock=1)
    assert "T1 - Test" in str(p)

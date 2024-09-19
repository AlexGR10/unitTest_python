import pytest
from src.main import ShoppingCart

def test_add_item():
    cart = ShoppingCart()
    cart.add_item("apple")
    assert cart.size() == 1
    assert cart.get_items() == ["apple"]

def test_size():
    cart = ShoppingCart()
    assert cart.size() == 0
    cart.add_item("apple")
    assert cart.size() == 1
    cart.add_item("banana")
    assert cart.size() == 2

def test_get_items():
    cart = ShoppingCart()
    cart.add_item("apple")
    cart.add_item("banana")
    items = cart.get_items()
    assert items == ["apple", "banana"]
    # Verificar que la lista devuelta es una copia
    items.append("cherry")
    assert cart.get_items() == ["apple", "banana"]

def test_empty_cart():
    cart = ShoppingCart()
    assert cart.size() == 0
    assert cart.get_items() == []

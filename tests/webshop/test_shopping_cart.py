"""Module for tests, src.webshop directory file: shopping_cart.

To test: Shopping Cart.
"""

#####################################################################
# Copyright 2026 gnoff
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#####################################################################


import pytest


from webshop.shopping_cart import ShoppingCart

from webshop.database import Database

from webshop.item import Item


# 1. We add an item to an empty shopping cart
# 2. We add a new item to a shopping cart that has other things
# 3. We add several items of the same kind to the shopping cart


# 'shovel', 50
# 'seeds', 25
# 'seeds', 25
#
# Item-class: name, price


@pytest.fixture(name='seeds')
def seeds_fixture():
    """Use to represent a specific seeds item."""
    return Item('seeds', 25)

@pytest.fixture(name='empty_cart')
def empty_cart_fixture():
    """Use to represent an empty shopping cart."""
    return ShoppingCart()

@pytest.fixture(name='cart')
def cart_fixture(db):
    """Use to handle a cart with item(s) already."""
    c = ShoppingCart()
    c.set_database(db)
    c.add_item(name='shovel', price=50)
    return c

@pytest.fixture(name='db')
def db_fixture(mocker):
    """Use to handle mocker database."""
    mock_db = mocker.Mock(spec=Database)
    mock_db.add_item_to_cart.return_value = None
    return mock_db

def test_shopping_cart__add_item_to_empty_cart(mocker, seeds,
                                               empty_cart):
    """Use to unit test add_item of Shopping_cart.

    Specifically test that we can add an item to an empty
    cart.
    US1, AC1, part 1.
    """
    # Arrange
    mock_db = mocker.Mock(spec=Database)
    mock_db.add_item_to_cart.return_value = None
    empty_cart.set_database(mock_db)

    # Act
    empty_cart.add_item(seeds.name, seeds.price)

    # Assert
    mock_db.add_item_to_cart.assert_called_once()
    mock_db.add_item_to_cart.assert_called_with(seeds.name,
                                                seeds.price)


def test_shopping_cart__add_item_to_cart(db, seeds, cart):
    """Use to unit test add_item of Shopping_cart.

    Specifically test that we can add an item to a cart
    that already contains at least one item.
    US1, AC1, part 2.
    """
    # Arrange
    cart.set_database(db)
    # Since the cart is not empty, add_item will have been called
    # more than once (in this case, exactly twice)
    expected_call_count = 1 + 1

    # Act
    cart.add_item(seeds.name, seeds.price)

    # Assert
    actual_call_count = db.add_item_to_cart.call_count
    assert actual_call_count == expected_call_count

    db.add_item_to_cart.assert_called_with(seeds.name, seeds.price)

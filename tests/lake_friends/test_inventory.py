"""Module for tests, src.lake_friends directory file: inventory.

To test: Inventory.
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


from lake_friends.inventory import Inventory

from lake_friends.database import Database

from lake_friends.item import Item



@pytest.fixture(name='canoe')
def canoe_fixture():
    """Use to represent a specific canoe item."""
    return Item(name='canoe', rent_price=250, amount=1)

@pytest.fixture(name='empty_db')
def empty_db_fixture():
    """Use to represent an empty inventory."""
    return Inventory()

@pytest.fixture(name='db_with_item')
def db_with_item_fixture(db):
    """Use to handle inventory with item(s) already."""
    inv = Inventory()
    inv.set_database(db)
    inv.set_item(name='tent', rent_price=150, amount=1)
    return inv

@pytest.fixture(name='db_inv')
def db_inv_fixture(mocker):
    """Use to handle mocker database of inventory."""
    mock_db_inv = mocker.Mock(spec=Database)
    mock_db_inv.add_item_to_db.return_value = None
    return mock_db_inv


def test_inventory__add_item_to_empty_inv(mocker, canoe, empty_db):
    """Use to unit test set_item of Inventory.

    Specifically test that we can add an item to an empty
    inventory.
    """
    # Arrange
    mock_db_inv = mocker.Mock(spec=Database)
    mock_db_inv.add_item_to_db.return_value = None
    empty_db.set_database(mock_db_inv)

    # Act
    empty_db.set_item(canoe.name, canoe.rent_price, canoe.amount)

    # Assert
    mock_db_inv.add_item_to_db.assert_called_once()
    mock_db_inv.add_item_to_db.assert_called_with(canoe.name,
                                                  canoe.rent_price,
                                                  canoe.amount)

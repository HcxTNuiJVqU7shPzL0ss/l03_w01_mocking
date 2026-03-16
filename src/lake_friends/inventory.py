"""Module for Lesson 03, Week 01, Lake Friends, Inventory.

Use for Inventory of "Vänerns Vänner".
Represents the association's inventory that members can rent.
- set_item(name, rent_price, amount)
- rent(item_name) # rent one item
- get_amount_left(name) # returns amount
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


class Inventory:
    """Use to represent the inventory of the association."""

    def __init__(self, database = None):
        """Use to initialize an object of the class Inventory."""
        self.database = database

    def set_database(self, database):
        """Use to set a database to use in inventory."""
        self.database = database

    def set_item(self, name, rent_price, amount):
        """Use to add an item to the database."""
        if self.database is None:
            raise RuntimeError('No database set')
        self.database.add_item_to_db(name, rent_price, amount)

"""Module for Lesson 03, Week 01, shopping_cart.

Use for Shopping Cart.
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


# User Story 1: As a customer, I want to be able to add a product
# to the shopping cart, so that I can purchase it.

# Acceptance Criteria:
# 1. There shall be a function to add a product in the database:
# add_item(name, price)
# (a more realistic example had used "id" instead)


class ShoppingCart:
    """Use to represent a shopping cart in a webshop."""

    def __init__(self, database = None):
        self.database = database

    def set_database(self, database):
        self.database = database

    def add_item(self, name, price):
        if self.database is None:
            raise RuntimeError('No database set')
        self.database.add_item_to_cart(name, price)

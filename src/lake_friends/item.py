"""Module for Lesson 03, Week 01, Lake Friends, Item.

Use for Item to handle inventory and database.
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


from dataclasses import dataclass


@dataclass()
class Item:
    """Use to store name, rent price amd amount of an item.

    To handle the association inventory that members can rent.
    """

    def __init__(self, name, rent_price, amount):
        """Use to initialize an object of class Item."""
        self.name = name
        self.rent_price = rent_price
        self.amount = amount

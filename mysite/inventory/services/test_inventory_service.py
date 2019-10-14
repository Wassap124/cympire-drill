import os
from .inventory_service import Inventory
from django.test import TestCase

dirname = os.path.dirname(__file__)
inventoryPath = os.path.join(dirname, '../common/mocks/inventory.txt')
class TestInventory(TestCase):
    def test_constructor_should_not_raise_error(self):
            Inventory("../file-that-doesnt.exists")
    def test_constructor_loads_json(self):
        inventroyManagement = Inventory(inventoryPath)

        # if inventory was set up correctly, this should always be an int
        assert type(inventroyManagement.get_median_for_category(10)) is int

    def test_get_categories_for_store(self):
        inventroyManagement = Inventory(inventoryPath)
        inventroyManagement._inventory = [
            { 'store': 1, 'category': 1}, 
            { 'store': 1, 'category': 2}, 
            { 'store': 2, 'category': 3}
        ]
        assert inventroyManagement.get_categories_for_store(1) == [1, 2]
    def test_get_categories_for_store_works_with_non_existing_store(self):
        inventroyManagement = Inventory(inventoryPath)
        inventroyManagement._inventory = [
            { 'store': 1, 'category': 1}, 
            { 'store': 1, 'category': 2}, 
            { 'store': 2, 'category': 3}
        ]
        assert inventroyManagement.get_categories_for_store(5) == []
    def test_get_item_inventory(self):
        inventroyManagement = Inventory(inventoryPath)
        inventroyManagement._inventory = [
            { 'store': 1, 'item_name': 'one'}, 
            { 'store': 1, 'item_name': 'two'}, 
            { 'store': 2, 'item_name': 'one'}
        ]
        x = inventroyManagement.get_item_inventory('one')
        assert len(x) == 2
        assert x[0] is inventroyManagement._inventory[0]
        assert x[1] is inventroyManagement._inventory[2]
    def test_get_item_inventory_non_existing_item(self):
        inventroyManagement = Inventory(inventoryPath)
        inventroyManagement._inventory = [
            { 'store': 1, 'item_name': 'one'}, 
            { 'store': 1, 'item_name': 'two'}, 
            { 'store': 2, 'item_name': 'one'}
        ]
        x = inventroyManagement.get_item_inventory('blah')
        assert len(x) == 0
    def test_get_median_for_category(self):
        inventroyManagement = Inventory(inventoryPath)
        inventroyManagement._inventory = [
            { 'category': 1, 'price': 1}, 
            { 'category': 1, 'price': 20}, 
            { 'category': 1, 'price': 100},
            { 'category': 2, 'price': 30}

        ]
        x = inventroyManagement.get_median_for_category(1)
        assert x ==20
    def test_get_median_for_category_when_there_are_two_medians(self):
        inventroyManagement = Inventory(inventoryPath)
        inventroyManagement._inventory = [
            { 'category': 1, 'price': 1}, 
            { 'category': 1, 'price': 20}, 

        ]
        x = inventroyManagement.get_median_for_category(1)

        # final median should be the average between the 2
        assert x == (1 + 20) / 2
    def test_get_median_for_category_for_non_existing_category(self):
        inventroyManagement = Inventory(inventoryPath)
        inventroyManagement._inventory = [
            { 'category': 1, 'price': 1}, 
            { 'category': 2, 'price': 20}, 

        ]
        x = inventroyManagement.get_median_for_category(3)

        assert x == 0

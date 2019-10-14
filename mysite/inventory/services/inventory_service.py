#!/usr/bin/python
import json
import statistics

class Inventory(object):
    """
    Inventory Management system 
    """
    def __init__(self, filePath):
        try:
            inventory = open(filePath, 'r')
            inventoryJson = inventory.read()
            self._inventory = json.loads(inventoryJson)
        except FileNotFoundError:
            print("Could not open mock file")
        except IOError:
            print("An error has occurred while trying to open the file")

    """
        Given a store id you should return all the categories ids in the inventory
    """
    def get_categories_for_store(self, store):
        storeItems = filter(lambda item: item['store'] == store, self._inventory)
        storeCategories = map( lambda item: item['category'], storeItems)
        uniqueCategories = []

        for category in storeCategories:
            if category not in uniqueCategories:
                uniqueCategories.append(category)

        return uniqueCategories

    """
        Given items name return all the items across all stores
    """
    def get_item_inventory(self, item):
        if (item == ''):
            return self._inventory

        return list(filter(lambda inventoryItem: inventoryItem['item_name'] == item, self._inventory))

    """
        Given category id return the median of the prices for all items in the category
    """
    def get_median_for_category(self, category):
        itemsByCategory = filter(lambda item: item['category'] == category, self._inventory)
        itemPrices = list(map( lambda item: item['price'], itemsByCategory))

        if len(itemPrices) == 0:
            return 0
        
        medianPrice = statistics.median(itemPrices)

        return medianPrice

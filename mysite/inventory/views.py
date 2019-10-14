import json
import os
from django.shortcuts import render
from django.http import HttpResponse
from .services.inventory_service import Inventory
# Create your views here.
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'common/mocks/inventory.txt')
inventory = Inventory(filename)

def displayJson (response):
    return json.dumps(response, separators=(':', ','))

def index(request):
    return HttpResponse("Hello, world. You're at the inventory index.")

def store_categories(request, store_id):
    response = inventory.get_categories_for_stroe(store_id)
    return HttpResponse(displayJson(response))

def item_by_name(request, item_name):
    response = inventory.get_item_inventory(item_name)
    return HttpResponse(displayJson(response))

def category_median(request, category_id):
    response = inventory.get_median_for_category(category_id)
    return HttpResponse(displayJson(response))
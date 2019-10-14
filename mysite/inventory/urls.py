from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stores/<int:store_id>/categories', views.store_categories ,name='store_categories'),
    path('items/<item_name>', views.item_by_name ,name='item_by_name'),
    path('categories/<int:category_id>/median', views.category_median ,name='category_median'),
]

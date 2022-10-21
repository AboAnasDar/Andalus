from django.urls import path
from .views import *

urlpatterns = [
    path('', welcome_page, name="welcome_page"),
    path('history/', history, name="history"),
    path('process/', process, name="process"),
    path('barren/', barren, name="barren"),
    path('categories/', categories, name="categories"),
    path('categories/delete/<str:id>/', delete_category, name="delete_category"),
    path('items/', items, name="items"),
    path('items/delete/<str:id>/', delete_item, name="delete_item"),
]

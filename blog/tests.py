from django.test import TestCase
# from itertools import count
# from unicodedata import category
# from .models import *

# # Create your tests here.


# class CategoryTestCase(TestCase):
#     def setUp(self):
#         Category.objects.create(title="Cate One")
#         Category.objects.create(title="Cate Two")

#     def test_title_equal_title(self):
#         one = Category.objects.get(title="Cate One")
#         two = Category.objects.get(title="Cate Two")
#         self.assertTrue(one)
#         self.assertTrue(two)


# class ItemTestCase(TestCase):
#     def setUp(self):
#         Item.objects.create(name="Item One", count=10)
#         Item.objects.create(name="Item Two", count=5)

#     def test_title_equal_title(self):
#         one = Item.objects.get(name="Item One")
#         two = Item.objects.get(name="Item Two")
#         self.assertTrue(one.count)
#         self.assertTrue(two.count)


# class HistoryTestCase(TestCase):
#     def setUp(self):
#         category = Category.objects.create(title="cate1")
#         item = Item.objects.create(name="item1", count=11)
#         History.objects.create(
#             category=category, item=item, number=10, process="add")

#     def test_title_equal_title(self):
#         category = Category.objects.filter(title="cate1")[0]
#         one = History.objects.filter(category=category)[0]
#         self.assertTrue(one.process)

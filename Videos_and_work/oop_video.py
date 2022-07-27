# # OOP Tutorial 7.26.22

from item import Item
# from phone import Phone

item1 = Item("MyItem", 750)

print(item1.name)

print(item1.read_only_name)

item1.read_only_name = 'BBB'
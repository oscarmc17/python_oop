# # OOP Tutorial 7.21.22

from item import Item
from phone import Phone

Item.instantiate_from_csv()

print(Item.all)


# When to use class methods and when to use statisc methods?

# class Item:
#     @staticmethod
#     def is_integer(num):
        
#     #    This should do something that has a relationship with a class,
#     #    but not something that must be unique per instance!

#         @classmethod
#         def instance_from_something(cls):
#             # This should do something that has a relationship with the class,
#             # but usually, those are used to manipulate different structures
#             # of data to instantiate objects, like we have done with CSV.
#             pass

# # OOP Tutorial 7.14.22
# import csv

# class Item:
#     pay_rate = 0.8 #The pay rate after 20% discount.
#     all = []

#     def __init__(self, name: str, price: float, quantity=0):
#         # Run validations to the received arguments
#         assert price >= 0, f"Price {price} is not greater than or equal to zero!"
#         assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
        
#         # Assign to self object
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#         # Actions to execute
#         Item.all.append(self)
        

#     def calculate_total_price(self):
#         return self.price * self.quantity
    
#     def apply_discount(self):
#         self.price = self.price * self.pay_rate
    
#     @classmethod
#     def instantiate_from_csv(cls):
#         with open('items.csv', 'r') as f:
#             reader = csv.DictReader(f)
#             items = list(reader)

#         for item in items:
#             Item(
#                 name = item.get('name'),
#                 price = float(item.get('price')),
#                 quantity = int(item.get('quantity')),
#             )

#     @staticmethod
#     def is_integer(num):
#         # We will count out the floats that are point zero. i.e: 5.0, 10.0.
#         if isinstance(num, float):
#             # Count out the floats that are point zero
#             return num.is_integer()
#         elif isinstance(num, int):
#             return True
#         else:
#             return False
        


#     def __repr__(self):
#         return f"Item('{self.name}', {self.price}, {self.quantity})"



# print(Item.is_integer(7.0))





# When to use class methods and when to use statisc methods?

class Item:
    @staticmethod
    def is_integer(num):
        
    #    This should do something that has a relationship with a class,
    #    but not something that must be unique per instance!

        @classmethod
        def instance_from_something(cls):
            # This should do something that has a relationship with the class,
            # but usually, those are used to manipulate different structures
            # of data to instantiate objects, like we have done with CSV.
            pass



# INHERITANCE
import csv

class Item:
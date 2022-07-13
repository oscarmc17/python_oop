# class Node:
#     # An object for storing a single node of a linked list.
#     # Models two attributes - data and the link to the next node in the list.

#     data = None
#     next_node = None

#     def __init__(self, data):
#         self.data = data

#     def __repr__(self):
#         return "<Node data: %s>" % self.data


# class LinkedList:
#     # Singly linked list

#     def __init__(self):
#         self.head = None

#     def is_empty(self):
#         return self.head == None

#     def size(self):
#         # Returns the number os nodes in the list. Takes 0(n) time.
#         current = self.head
#         count = 0 

#         while current:
#             count += 1
#             current = current.next_node

#         return count


#     def add(self,data):
#         # Adds new Node containing data at head of the list.
#         # Takes 0(1) time
#         new_node = Node(data)
#         new_node.next_node = self.head
#         self.head = new_node
    

#     def search(self, key):
#         # Search for the first node containing data that 
#         # matches they key. Returns the node or 'None" if not found
#         # Takes 0(n) time
#         current = self.head

#         while current:
#             if current.data == key:
#                 return current
#             else:
#                 current = current.next_node
#         return None

#     def __repr__(self):
#     # Return a string representation of the list.
#     # Takes 0(n) time
#         nodes = []
#         current = self.head

#         while current:
#             if current is self.head:
#                 nodes.append("[head: %s]" % current.data)
#             elif current.next_node is None:
#                 nodes.append("[Tail: %s]" % current.data)
#             else:
#                 nodes.append("[%s]" % current.data)
            
#             current = current.next_node
#         return '-> '.join(nodes)


# OOP Tutorial 7.5.22
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

#     def __repr__(self):
#         return f"Item('{self.name}', {self.price}, {self.quantity})"

# # item1 = Item("Phone", 100, 1)
# # item2 = Item("Laptop", 1000, 3)
# # item3 = Item("Cable", 10, 5)
# # item4 = Item("Mouse", 50, 5)
# # item5 = Item("Keyboard", 75, 5)

# # print(Item.all)

# Item.instantiate_from_csv()
# print(Item.all)




# MY OWN WORK

# class Employee:

#     raise_amount = 1.04

#     def __init__(self, name, age, company, pay):
#         self.name = name
#         self.age = age
#         self.company = company   
#         self.pay = pay

#     def full(self):
#         return f"{self.name} {self.age} {self.company} {self.pay}"

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)

# person1 = Person("Oscar Caicedo", 27, "Epsilon", 80000)
# person2 = Person("Rogelio Mitre", 22, "Meta", 67000)
# person3 = Person("Jose Armas", 26, "Twitter", 75000)

# person1.raise_amount = 1.05

# print(person1.__dict__)

# print(Person.raise_amount)
# print(person1.raise_amount)
# print(person2.raise_amount)

# print(person1.full())
# print(person2.full())
# print(person3.full())

# print(Person.full(person1))
# print(Person.full(person2))
# print(Person.full(person3))






class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

# Employee.set_raise_amt(1.05)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

# MY OWN WORK

class Employee:

    raise_amount = 1.04

    def __init__(self, name, age, company, pay):
        self.name = name
        self.age = age
        self.company = company   
        self.pay = pay

    def full(self):
        return f"{self.name} {self.age} {self.company} {self.pay}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

person1 = Person("Oscar Caicedo", 27, "Epsilon", 80000)
person2 = Person("Rogelio Mitre", 22, "Meta", 67000)
person3 = Person("Jose Armas", 26, "Twitter", 75000)
# 
person1.raise_amount = 1.05

print(person1.__dict__)

print(Person.raise_amount)
print(person1.raise_amount)
print(person2.raise_amount)

print(person1.full())
print(person2.full())
print(person3.full())

print(Person.full(person1))
print(Person.full(person2))
print(Person.full(person3))
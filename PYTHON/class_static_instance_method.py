"""
Naming these parameters self and cls is just a convention. You could just as easily name them the_object and the_class and get the same result. All that matters is that they’re positioned first in the parameter list for the method.
"""

import math


class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


obj = MyClass()
print(obj.method())
print(MyClass.method(obj))
print(obj.classmethod())
print(obj.staticmethod())


class Pizza:
    def __init__(self, ingredients, radius=None):
        self.ingredients = ingredients
        self.radius = radius
        
    def area(self):
        return self.circle_area(self.radius)
    
    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'
    
    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])
    

obj = Pizza(['cheese', 'tomatoes'])
obj2 = Pizza(['mozzarella', 'tomatoes', 'ham', 'mushrooms'])
obj3 = Pizza(['mozzarella'] * 4)

print(obj)
print(obj2)
print(obj3)
print(Pizza.margherita())
print(Pizza.prosciutto())

p = Pizza(['mozzarella', 'tomatoes'], 4)

print(p.area())

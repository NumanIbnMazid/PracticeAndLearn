

class Dog():
    # Class Object Attribute
    # Same for any instances for a class
    species = 'mammal'

    # init doesn't return anything. It's a constructor.
    def __init__(self, breed, name, spots):
        # Attributes
        # Take in the argument 
        # Assign it using self.attribute_name
        # Class instance Attribute
        self.breed = breed
        self.name = name
        self.spots = spots

    # Methods -> Functions of a class -> Operations/Actions
    def bark(self, number):
        return "WOOF! My name is {}. The number is {}.".format(self.name, number)

my_dog = Dog(breed='Lab', name='Sammy', spots=False)

print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)
print(my_dog.bark(10))

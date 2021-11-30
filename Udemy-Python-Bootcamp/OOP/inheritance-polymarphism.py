
# Inheritance 

class Animal():

    def __init__(self):
        # init doesn't return anything. It's a constructor.
        print("Animal Created.")

    def who_am_i(self):
        return "I am an Animal."

    def eat(self):
        return "I am eating."


class Dog(Animal):

    def __init__(self, name):
        # Inheritance Here
        Animal.__init__(self)
        print("Dog Created.")
        self.name = name

    # Overwrite inherited method.
    def who_am_i(self):
        return "I am a Dog."

    def bark(self):
        return "WOOF!!!"

    def speak(self):
        return f"{self.name} says {self.bark()}"
    

    
my_dog = Dog(name="Nikki")

print(my_dog)
print(my_dog.who_am_i())
print(my_dog.eat())
print(my_dog.bark())

# Polymarphism


class Cat(Animal):

    def __init__(self, name):
        # Inheritance Here
        Animal.__init__(self)
        print("Cat Created.")
        self.name = name

    # Overwrite inherited method.
    def who_am_i(self):
        return "I am a Cat."

    def meow(self):
        return "MEOW!!!"

    def speak(self):
        return f"{self.name} says {self.meow()}"


bob = Dog("Alan")
felix = Cat("Ena")

print(bob.speak())
print(felix.speak())

print("\n----------------")

for pet in [bob, felix]:
    print(type(pet))
    print(pet.speak())


def pet_speak(pet):
    return pet.speak()


print(pet_speak(bob))
print(pet_speak(felix))



print("\n-------------------")

class Human():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method!")


class Girl(Human):

    def speak(self):
        return f"{self.name} says, I am a girl!"

class Boy(Human):

    def speak(self):
        return f"{self.name} says, I am a boy!"

numan = Boy('Numan')
disha = Girl('Disha')

print(numan.speak())
print(disha.speak())

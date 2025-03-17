# polymorphism implementation
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
        
    def make_sound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Dodo", 2.5)   
cat2 = Cat("Kitty", 3)
dog1 = Dog("Tyson", 8)
dog2 = Dog("Tommy", 5)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()

for animal in (cat2, dog2):
     animal.make_sound()
     animal.info()

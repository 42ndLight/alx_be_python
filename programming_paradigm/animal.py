class Dog:
    def make_sound(self):
        print('Bark! Bark! Bark!')

class Cat:
    def make_sound(self):
        print('Meow! Meow! Meow!')

class Bird:
    def make_sound(self):
        print('Chirp! Chirp! Chirp!')

def make_sound(obj):
    obj.make_sound()


animals = [Dog(), Cat(), Bird()]
for animal in animals:
    make_sound(animal)
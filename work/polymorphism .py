#polymorphism
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


class Bird(Animal):
    def make_sound(self):
        print("Tweet!")


def main():
    animals = [Dog("Fido"), Cat("Garfield"), Bird("Tweety")]

    for animal in animals:
        animal.make_sound()


if __name__ == "__main__":
    main()

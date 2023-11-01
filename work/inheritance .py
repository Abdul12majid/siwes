#inheritance
class Animal(object):
  def __init__(self, name, sound):
    self.name = name
    self.sound = sound

  def make_sound(self):
    print(f"{self.name} says {self.sound}.")

class Dog(Animal):
  def __init__(self, name, breed):
    super().__init__(name, "Woof!")
    self.breed = breed

  # Overriding the `make_sound()` method
  def make_sound(self):
    print(f"{self.breed} {self.name} says Woof!")

class Cat(Animal):
  def __init__(self, name, fur_color):
    super().__init__(name, "Meow!")
    self.fur_color = fur_color

  # Overriding the `make_sound()` method
  def make_sound(self):
    print(f"{self.fur_color} {self.name} says Meow!")

# Create a new Dog object
dog = Dog("Fido", "Golden Retriever")

# Make the dog bark
dog.make_sound()

# Create a new Cat object
cat = Cat("Whiskers", "Black")

# Make the cat meow
cat.make_sound()

# Create a class called `Shape`
class Shape:
  def __init__(self, name):
    self.name = name

  def calculate_area(self):
    pass

# Create a class called `Rectangle` that inherits from the `Shape` class
class Rectangle(Shape):
  def __init__(self, length, width):
    super().__init__(name="Rectangle")
    self.length = length
    self.width = width

  def calculate_area(self):
    return self.length * self.width

# Create a new Rectangle object
rectangle = Rectangle(length=10, width=5)

# Calculate the area of the rectangle
rectangle_area = rectangle.calculate_area()

# Print the area of the rectangle
print(f"The area of the rectangle is {rectangle_area}.")

# Create a class called `Circle` that inherits from the `Shape` class
class Circle(Shape):
  def __init__(self, radius):
    super().__init__(name="Circle")
    self.radius = radius

  def calculate_area(self):
    return math.pi * self.radius ** 2

# Create a new Circle object
circle = Circle(radius=5)

# Calculate the area of the circle
circle_area = circle.calculate_area()

# Print the area of the circle
print(f"The area of the circle is {circle_area}.")

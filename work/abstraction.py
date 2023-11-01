#abstraction
class AbstractVehicle:
  """An abstract class for vehicles.

  This class defines the common interface for all vehicles.
  """

  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

  def accelerate(self):
    """Abstract method for accelerating the vehicle."""
    raise NotImplementedError()

  def brake(self):
    """Abstract method for braking the vehicle."""
    raise NotImplementedError()

  def turn(self, direction):
    """Abstract method for turning the vehicle in a given direction.

    Args:
      direction: The direction to turn the vehicle in.
    """
    raise NotImplementedError()


class Car(AbstractVehicle):
  """A concrete class for cars.

  This class inherits from the AbstractVehicle class and implements the
  abstract methods for accelerating, braking, and turning.
  """

  def accelerate(self):
    """Accelerates the car."""
    print(f"{self.make} {self.model} is accelerating.")

  def brake(self):
    """Brakes the car."""
    print(f"{self.make} {self.model} is braking.")

  def turn(self, direction):
    """Turns the car in a given direction.

    Args:
      direction: The direction to turn the car in.
    """
    print(f"{self.make} {self.model} is turning {direction}.")


class Truck(AbstractVehicle):
  """A concrete class for trucks.

  This class inherits from the AbstractVehicle class and implements the
  abstract methods for accelerating, braking, and turning.
  """

  def accelerate(self):
    """Accelerates the truck."""
    print(f"{self.make} {self.model} is accelerating slowly.")

  def brake(self):
    """Brakes the truck."""
    print(f"{self.make} {self.model} is braking slowly.")

  def turn(self, direction):
    """Turns the truck in a given direction.

    Args:
      direction: The direction to turn the truck in.
    """
    print(f"{self.make} {self.model} is turning {direction} with difficulty.")


def main():
  """Creates a car and a truck and calls their methods."""

  car = Car("Toyota", "Camry", 2023)
  truck = Truck("Ford", "F-150", 2023)

  car.accelerate()
  car.brake()
  car.turn("left")

  truck.accelerate()
  truck.brake()
  truck.turn("right")


if __name__ == "__main__":
  main()

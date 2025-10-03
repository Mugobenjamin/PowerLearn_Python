# Base class
class Vehicle:
    def move(self):
        # General move method (can be overridden)
        print("The vehicle is moving...")

# Subclasses with different implementations of move()
class Car(Vehicle):
    def move(self):
        print("Driving on the road...")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky...")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water...")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the street...")

vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    v.move()   # Each class runs its own version of move()

# Parent Class (Base Class)
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model} ka engine start ho gaya.")

    def stop_engine(self):
        print(f"{self.brand} {self.model} ka engine band ho gaya.")

# Child Class (Derived Class)
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # Parent class ka constructor call
        self.doors = doors

    # Method Overriding
    def start_engine(self):
        print(f"{self.brand} {self.model} (Car) ka engine smoothly start ho gaya.")

    def show_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Doors: {self.doors}")

# Object Creation
v1 = Vehicle("Honda", "Shine")
v1.start_engine()
v1.stop_engine()

print("-----")

c1 = Car("Toyota", "Fortuner", 4)
c1.start_engine()
c1.show_details()
c1.stop_engine()

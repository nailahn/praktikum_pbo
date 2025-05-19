#make class Vehicle
class Vehicle:
	def __init__(self, brand, model, year):
		self.brand = brand
		self.model = model
		self.year = year

#make methods
	def start(self):
		print("vehicle is starting")
	def stop(self):
		print("vehicle is stopping")
#define sub class and make class Car (inheritance from Vehicle)
# the super() to call method __init__() from class Vehicle
class Car(Vehicle):
	def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
		super().__init__(brand, model, year)
		self.number_of_doors= number_of_doors
		self.number_of_wheels=number_of_wheels

#make class Bike (inheritance from Vehicle)
class Bike(Vehicle):
	def __init__(self, brand, model, year, number_of_wheels):
		super().__init__(brand, model, year)
		self.number_of_wheels=number_of_wheels

#make object
car = Car("Ford", "Focus", 2008, 5, 4)
bike = Bike("Honda", "Scoopy", 2018, 2)
#print attribute dan method
print(car.__dict__)
print(bike.__dict__)
car.start()
bike.start()

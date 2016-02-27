class Car(object):
	def __init__(self, speed, fuel, mileage, price):
		self.speed = speed 
		self.fuel = fuel
		self.mileage = mileage
		self.price = price
		if price > 10000:
		   self.tax = .15
		else:
		    self.tax = .12
		self.display_all()

	def display_all(self):
		print "Price: " + str(self.price)
		print "Speed: " + str(self.speed) + "mph"
		print "Fuel: " + str(self.fuel)
		print "Mileage: " + str(self.mileage) + "mpg"
		print "Tax: " + str(self.tax)

car1 = Car(20000, 40, "Half-Full", 90)
car2 = Car(9000, 30, "Full", 80)
car3 = Car(400, 20, "Empty", 70)
car4 = Car(7000, 50, "Full", 90)
car5 = Car(800, 50, "Half-Full", 90)

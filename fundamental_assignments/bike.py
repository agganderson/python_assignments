class Bike(object):
	def __init__(self, price, max_speed, mile = 0):
		print "New bike!"
		self.price = price
		self.max_speed = max_speed
		self.mile = mile

	def displayInfo(self):
		print "Your bike cost " + str(self.price) + ", your max speed was " + str(self.max_speed) + ", and your total miles ridden is " + str(self.mile)

	def ride(self):
		print "Riding..."
		self.mile = self.mile + 10
		print "You have gone " + str(self.mile) + " miles. Good o."

	def reverse(self):
		print "Reversing..."
		if self.mile >= 5:
			self.mile -= 5
		print "You have gone back " + str(self.mile) + " miles..."

bike1 = Bike(100, 20)
decision = raw_input("Ready?")
if(decision == "yes"):
	bike1.ride()
	print ".. Keep goin.."
	bike1.ride()
	print "Almost done!"
	bike1.ride()
else:
	print "Get to it!"

decision = raw_input("Go back?")
if(decision == "yes"):
	bike1.reverse()
	print "What happened?"
	bike1.displayInfo()
else:
	print "Just do it"

bike2 = Bike(200, 40)
decision = raw_input("Go again?")
if(decision == "yes"):
	bike2.ride()
	print "Keep goingggg"
	bike2.ride()
	print "And now?"
	bike2.reverse()
	print "Why are you reversing?"
	bike2.reverse()
	print "Feel better?"
	bike2.displayInfo()
else:
	print "Why?"

bike3 = Bike(300, 50)
decision = raw_input("Backwards?")
if(decision == "yes"):
	bike3.reverse()
	print "One more time"
	bike3.reverse()
	print "Done"
	bike3.displayInfo()
else:
	print "please just say yes"





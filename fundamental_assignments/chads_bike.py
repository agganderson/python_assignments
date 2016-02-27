import random
class Bike(object):
	def __init__(self, price, max_speed, miles = 0):
		print "Bike Generated!"
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
​
	def displayInfo(self):
		print 'You have gone ' + str(self.miles) + ' miles, your max speed was ' + str(self.max_speed) + ' Your bike cost you ' + str(self.price)  
​
	def ride(self):
		print 'Riding'
		self.miles = self.miles + 10
		print 'This bike has gone ' + str(self.miles) + ' miles' 
​
	def reverse(self):
		print 'Reversing'
		self.miles = self.miles - 5
		print 'This bike has gone ' + str(self.miles) + ' miles'
​
bike1 = Bike(200, 30,)
decision = raw_input("Ready to ride?!")
if(decision == "yes"):
	bike1.ride()
else:
	print 'Stop being lazy!'
​
bike2 = Bike(300, 25)
answer = raw_input("Are you ready to ride in reverse, biker number two?!")
if(answer == 'yes'):
	bike2.reverse()
else:
	print 'Lets see those skills you got!'
bike3 = Bike(500, 50)
rider_answer = raw_input('Can you tell us all the specs on your bike, please?!')
if(rider_answer == 'yes'):
	bike3.displayInfo()
else:
	print 'We want INFORMATION!!!'
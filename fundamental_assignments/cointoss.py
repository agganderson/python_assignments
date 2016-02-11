import random
import math

print "Starting the program"

head_count = 0
tail_count = 0
for i in range(0, 11):
	rand = round(random.random())
	if rand == 0:
		face = 'tail' 
		tail_count += 1
	else:
		face = 'head'
		head_count += 1
	print "Attempt #" + str(i) + ": Throwing a coin...it's a " + face + "!..." + str(head_count) + " head(s) so far and " + str(tail_count) + " tail(s) so far"
print "Ending the program, thank you!"
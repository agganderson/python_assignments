oddeven_list=list(range(1, 21))
for i in oddeven_list:
	if i < 21:
		print "Number is", i
	if i % 2 !=  0:
		print "This number is odd."
	if i % 2 == 0:
		print "This number is even."

OR

for i in range(1,2001):
    if i % 2 == 0:
        print 'Number is ' + str(i) + '. This is an odd number.'
    else:
        print 'Number is ' + str(i) + '. This is an even number.'
